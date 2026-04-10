import aiosqlite
import json
from datetime import datetime
from typing import Optional, List, Dict, Any

DB_PATH = "./farmvoice.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS diagnoses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                transcript TEXT,
                detected_language TEXT,
                primary_disease TEXT,
                confidence INTEGER,
                severity INTEGER,
                urgency TEXT,
                latitude REAL,
                longitude REAL,
                diagnosis_json TEXT,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                feedback_type TEXT NOT NULL,
                actual_disease TEXT,
                farmer_note TEXT,
                helpful_rating INTEGER,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES diagnoses(session_id)
            )
        """)
        await db.execute("CREATE INDEX IF NOT EXISTS idx_diagnoses_session ON diagnoses(session_id)")
        await db.execute("CREATE INDEX IF NOT EXISTS idx_diagnoses_timestamp ON diagnoses(timestamp)")
        await db.execute("CREATE INDEX IF NOT EXISTS idx_feedback_session ON feedback(session_id)")
        await db.commit()


async def save_diagnosis(
    session_id: str,
    transcript: str,
    detected_language: str,
    primary_disease: str,
    confidence: int,
    severity: int,
    urgency: str,
    latitude: Optional[float],
    longitude: Optional[float],
    diagnosis_json: Dict[str, Any],
):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO diagnoses
            (session_id, transcript, detected_language, primary_disease,
             confidence, severity, urgency, latitude, longitude, diagnosis_json, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session_id,
                transcript,
                detected_language,
                primary_disease,
                confidence,
                severity,
                urgency,
                latitude,
                longitude,
                json.dumps(diagnosis_json),
                datetime.utcnow().isoformat(),
            ),
        )
        await db.commit()


async def save_feedback(
    session_id: str,
    feedback_type: str,
    actual_disease: Optional[str],
    farmer_note: Optional[str],
    helpful_rating: Optional[int],
):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT INTO feedback (session_id, feedback_type, actual_disease, farmer_note, helpful_rating, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (session_id, feedback_type, actual_disease, farmer_note, helpful_rating, datetime.utcnow().isoformat()),
        )
        await db.commit()


async def get_history(limit: int = 20) -> List[Dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """
            SELECT d.session_id, d.transcript, d.primary_disease, d.confidence,
                   d.severity, d.urgency, d.timestamp, f.feedback_type
            FROM diagnoses d
            LEFT JOIN feedback f ON d.session_id = f.session_id
            ORDER BY d.timestamp DESC
            LIMIT ?
            """,
            (limit,),
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def get_feedback_stats() -> Dict[str, Any]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) as total FROM diagnoses") as cursor:
            total_row = await cursor.fetchone()
        async with db.execute(
            "SELECT feedback_type, COUNT(*) as count FROM feedback GROUP BY feedback_type"
        ) as cursor:
            feedback_rows = await cursor.fetchall()
        async with db.execute("SELECT AVG(helpful_rating) as avg_rating FROM feedback WHERE helpful_rating IS NOT NULL") as cursor:
            rating_row = await cursor.fetchone()

    feedback_breakdown = {row[0]: row[1] for row in feedback_rows} if feedback_rows else {}
    return {
        "total_diagnoses": total_row[0] if total_row else 0,
        "feedback_breakdown": feedback_breakdown,
        "avg_helpfulness": round(rating_row[0], 2) if rating_row and rating_row[0] else None,
    }
