from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

from app.routes import ingest, chat, summerize, analyze, sources, health

app = FastAPI(
    title = "AI Research Assistant API",
    description = "RAG-powered API for ingesting and querying any topic using LLMs",
    version = "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(ingest.router, prefix="/api", tags=["Ingest"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(summerize.router, prefix="/api", tags=["Summary"])
app.include_router(analyze.router, prefix="/api", tags=["Analyze"])
app.include_router(sources.router, prefix="/api", tags=["Source"])
app.include_router(health.router, prefix="/api", tags=["Health"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Research Assistant API",
    "docs": "/docs",
    "health": "/api/health"}
