from pydantic import BaseModel
from typing import Optional, List


class IngestRequest(BaseModel):
    topic: str
    source_type: Optional[str] = "web"


class IngestResponse(BaseModel):
    status: str
    chunks_stored: int
    source: str
    message: str


class ChatRequest(BaseModel):
    query: str
    session_id: Optional[str] = "default"


class ChatResponse(BaseModel):
    response: str
    sources_used: int
    session_id: str


class SummarizeRequest(BaseModel):
    topic: str
    summary_type: Optional[str] = "key_insights"


class SummarizeResponse(BaseModel):
    summary: str
    key_points: List[str]
    word_count: int


class AnalyzeRequest(BaseModel):
    topic: str
    analysis_type: Optional[str] = "statistical"


class AnalyzeResponse(BaseModel):
    analysis: str
    metrics: dict
    visualizations: Optional[str] = None


class SourceInfo(BaseModel):
    topic: str
    chunks: int
    ingested_at: str


class SourcesResponse(BaseModel):
    total_sources: int
    sources: List[SourceInfo]


class HealthResponse(BaseModel):
    status: str
    version: str
    message: str