from fastapi import APIRouter

router = APIRouter()

@router.post("/summerize")
async def summerize():
    return {"message": "Summerizing..."}