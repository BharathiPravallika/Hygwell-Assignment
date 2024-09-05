from fastapi import FastAPI
from app.routes import process_url, process_pdf, chat

app = FastAPI()

#Register API routes
app.include_router(process_url.router)
app.include_router(process_pdf.router)
app.include_router(chat.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend service"}

#This part is to start the app using Uvicorn
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port = 8000)