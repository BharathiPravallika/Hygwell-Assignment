# from pydantic import BaseModel

# class ChatRequest(BaseModel):
#     chat_id: str
#     question: str

# class ChatResponse(BaseModel):
#     response: str


from sqlalchemy import Column, String, Text
from app.database import Base

class Chat(Base):
  __tablename__ = "chats"

  chat_id = Column(String, primary_key=True, index=True)
  content = Column(Text, index=True)
