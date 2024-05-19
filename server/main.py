from fastapi import FastAPI, HTTPException, Response, UploadFile
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import Union, List
from loguru import logger
from socket_io import init_socketio, socket_router
from routes.file import file_router

app = FastAPI()


@app.get("/ping")
def ping():
    return {"ping": "pong"}


app.include_router(socket_router)
app.include_router(file_router)
init_socketio(app)

logger.info("server init")

if __name__ == "__main__":
    ...
