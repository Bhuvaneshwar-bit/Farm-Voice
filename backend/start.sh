#!/bin/bash
# FarmVoice Backend Startup Script

set -e

echo "🌾 Starting FarmVoice Backend..."

# Check .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Copying from .env.example..."
    cp .env.example .env
    echo "✏️  Please edit .env and add your ANTHROPIC_API_KEY, then run again."
    exit 1
fi

# Install dependencies if needed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate || source venv/Scripts/activate

echo "📦 Installing dependencies..."
pip install -r requirements.txt -q

echo "🚀 Starting server on http://localhost:8000"
echo "📖 API docs at http://localhost:8000/docs"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
