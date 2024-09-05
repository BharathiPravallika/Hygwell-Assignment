from fastapi import APIRouter, File, UploadFile, HTTPException
from app.utils.pdf_processing import extract_text_from_pdf
import uuid
from app.storage import storage #Import shared storage

router = APIRouter()

@router.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    print("Storage dictionary before use:", storage)
    content = extract_text_from_pdf(file.file)
    print("PDF Content:", content)
    if not content:
        raise HTTPException(status_code=400, detail="Could not extract text from PDF")

    chat_id = str(uuid.uuid4())
    storage[chat_id] = content

    print("Storage dictionary after PDF processing:", storage)
    return {"chat_id": chat_id, "message": "PDF content processed and stored successfully."}
