from db import get_mongodb, get_vectory
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from routes.chat import chat_router
from routes.file import file_router
from routes.text import text_router
from routes.vector import vector_router
from socket_io import init_socketio, socket_router

load_dotenv()
get_vectory()
get_mongodb()

app = FastAPI()


@app.get("/ping")
def ping():
    return {"ping": "pong"}


origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://tauri.localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(socket_router)
app.include_router(file_router)
app.include_router(chat_router)
app.include_router(text_router)
app.include_router(vector_router)
init_socketio(app)

logger.info("server init")

if __name__ == "__main__":
    ...
