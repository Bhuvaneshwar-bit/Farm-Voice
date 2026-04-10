import chromadb
from chromadb.utils import embedding_functions
from typing import List, Optional
from app.core.config import settings

_client = None
_collection = None


def get_chroma_client():
    global _client
    if _client is None:
        _client = chromadb.PersistentClient(path=settings.CHROMA_DB_PATH)
    return _client


def get_collection():
    global _collection
    if _collection is None:
        client = get_chroma_client()
        ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        _collection = client.get_or_create_collection(
            name="farmvoice_knowledge",
            embedding_function=ef,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection


def is_knowledge_base_populated() -> bool:
    try:
        collection = get_collection()
        return collection.count() > 0
    except Exception:
        return False


def populate_knowledge_base(documents: List[dict]):
    """Load the agricultural knowledge base into ChromaDB."""
    collection = get_collection()
    if collection.count() > 0:
        return  # already populated

    texts = [doc["content"] for doc in documents]
    ids = [doc["id"] for doc in documents]
    metadatas = [{"crop": doc.get("crop", ""), "type": doc.get("type", ""), "title": doc.get("title", "")} for doc in documents]

    batch_size = 50
    for i in range(0, len(texts), batch_size):
        collection.add(
            documents=texts[i : i + batch_size],
            ids=ids[i : i + batch_size],
            metadatas=metadatas[i : i + batch_size],
        )
    print(f"Knowledge base populated with {len(texts)} documents.")


def query_knowledge_base(query: str, crop_hint: Optional[str] = None, n_results: int = 5) -> str:
    """Retrieve relevant agricultural knowledge for a given query."""
    try:
        collection = get_collection()
        if collection.count() == 0:
            return "No knowledge base available."

        where_filter = None
        if crop_hint:
            where_filter = {"crop": {"$eq": crop_hint.lower()}}

        results = collection.query(
            query_texts=[query],
            n_results=min(n_results, collection.count()),
            where=where_filter if where_filter else None,
        )

        if not results["documents"] or not results["documents"][0]:
            results = collection.query(query_texts=[query], n_results=min(n_results, collection.count()))

        docs = results["documents"][0] if results["documents"] else []
        return "\n\n---\n\n".join(docs[:n_results])
    except Exception as e:
        print(f"RAG query error: {e}")
        return "Knowledge base query failed."
