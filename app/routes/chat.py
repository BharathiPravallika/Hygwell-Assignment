from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from app.utils.embeddings import get_embedding, find_most_relevant_section
import numpy as np
from typing import Dict
import logging
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Chat
from app.storage import storage #Import shared storage

logging.basicConfig(level=logging.DEBUG)
router = APIRouter()

class ChatRequest(BaseModel):
    chat_id: str
    question: str

@router.post("/chat")
async def chat(request: ChatRequest):
    # Check if the chat_id exists in the storage
    logging.debug(f"Storage content: {storage}") #log storage content
    print("Received chat_id:", request.chat_id)
    print("Current storage content:", storage)
    
    if request.chat_id not in storage:
        raise HTTPException(status_code=404, detail="Chat ID not found")

    # Get the stored content for the chat_id
    content = storage[request.chat_id]
    return {"content": content}