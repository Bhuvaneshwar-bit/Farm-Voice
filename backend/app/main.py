from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.models.database import init_db
from app.core.rag import populate_knowledge_base, is_knowledge_base_populated
from app.data.knowledge_base import get_all_documents
from app.api.routes import diagnosis, feedback, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("FarmVoice API starting up...")
    await init_db()
    print("Database initialized.")

    if not is_knowledge_base_populated():
        print("Populating agricultural knowledge base (first run)...")
        docs = get_all_documents()
        populate_knowledge_base(docs)
        print(f"Knowledge base ready: {len(docs)} documents loaded.")
    else:
        print("Knowledge base already populated.")

    yield
    # Shutdown
    print("FarmVoice API shutting down.")


app = FastAPI(
    title="FarmVoice API",
    description="Multilingual AI Field Assistant for Smallholder Farmers",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1", tags=["Health"])
app.include_router(diagnosis.router, prefix="/api/v1", tags=["Diagnosis"])
app.include_router(feedback.router, prefix="/api/v1", tags=["Feedback"])


@app.get("/")
async def root():
    return {
        "service": "FarmVoice",
        "tagline": "Multilingual AI Field Assistant for Smallholder Farmers",
        "docs": "/docs",
        "health": "/api/v1/health",
    }
