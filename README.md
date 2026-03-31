# AI-research-assitant-api

A production - raady REST API that enables RAG - powered conversations querying over any ingested topic using LLMs. 

## What it does 
- Ingest any topic.
- feteches web data
- stores in vector database
- chat with ingested data using natural langauge
- summerzie and extract structured insights
- OpenAI LLM support
  
## Tech Stack 
- **Backend:**  FastAPI, Python, Uvicorn
- **AI/LLM:**   OpenAI API, LangChain
- **Vector DB :**  ChromaDB (RAG Pipleline)
- **Data:**  Pandas, NumPY
- **Deployment:** Docker, Google Cloud Run
- **Other:**  Pydantic, python-dotenv, GitHub Actions
## API Endpoints 
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/health | Health check |
| POST | /api/ingest | Ingest topic into vector DB |
| POST | /api/chat | Conversational RAG query |
| POST | /api/summarize | Summarize ingested data |
| POST | /api/analyze | Statistical analysis |
| GET | /api/sources | List ingested sources |

## Status
Active Development - endpoints live, RAG pipeline in progress

## Run Locally
```bash
git clone https://github.com/yourusername/ai-research-assistant-api
cd ai-research-assistant-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
