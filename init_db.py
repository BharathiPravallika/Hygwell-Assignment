from app.database import engine, Base
from app.models import Chat

Base.metadata.create_all(bind=engine)

