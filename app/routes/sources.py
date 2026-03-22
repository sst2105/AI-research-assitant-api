from fastapi import APIRouter

router = APIRouter()

@router.get("/sources")
async def get_sources():
    return {"message": "Getting sources..."}