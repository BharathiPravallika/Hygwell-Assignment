from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.scraping import scrape_content
import uuid
from app.storage import storage #Import shared storage

router = APIRouter()

class URLRequest(BaseModel):
    url: str

@router.post("/process_url")
async def process_url(request: URLRequest):
    content = scrape_content(request.url)
    if not content:
        raise HTTPException(status_code=404, detail="Content could not be scraped")
    chat_id = str(uuid.uuid4())
    storage[chat_id] = content
    print("Storage dictionary after URL processing:", storage)
    return {"chat_id": chat_id, "message": "URL content processed and stored successfully."}
