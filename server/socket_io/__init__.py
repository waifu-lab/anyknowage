import os

import socketio
from fastapi import APIRouter
from loguru import logger
from models.notify_leve import NotifyRequest

pwd_path = os.path.dirname(os.path.abspath(__file__))
socket_router = APIRouter(prefix="/socketio")
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=[],
)


@socket_router.post("/notify")
async def notify(request: NotifyRequest):
    """
    通知所有連接的client
    """
    await sio.emit("notify", request.model_dump(), namespace="/")
    return {"status": "ok"}


def init_socketio(app):
    async def connect(sid, environ):
        await sio.emit("reply", "Some server已連接", namespace="/")

    async def message(sid, data):
        await sio.emit("reply", f"{data}", namespace="/")

    async def disconnect(sid):
        await sio.emit("reply", "Some server已斷線", namespace="/")

    sio.on("disconnect", disconnect, namespace="/")
    sio.on("chat message", message, namespace="/")
    sio.on("connect", connect, namespace="/")
    app.mount("/", socketio.ASGIApp(socketio_server=sio))
    logger.info("socketio init")
