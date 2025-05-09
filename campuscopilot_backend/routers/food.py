from fastapi import APIRouter, Query
from utils.google_places import search_places

router = APIRouter()

@router.get("/")
def food_search(q: str = Query(..., description="Search query, e.g. 'best dosa near hostel'")):
    results = search_places(q)
    return results