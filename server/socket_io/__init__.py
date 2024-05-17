import os
import socketio
from bidict import bidict
from fastapi import APIRouter
from loguru import logger

pwd_path = os.path.dirname(os.path.abspath(__file__))
server_sid = bidict()
socket_router = APIRouter()


def init_socketio(app):
    async def connect(sid, environ):
        servername = 'test'
        server_sid[servername] = sid
        await sio.emit('reply', f'{servername}已連接', namespace='/socketio')

    async def message(sid, data):
        await sio.emit('reply', f"{server_sid.inv[sid]}: {data}", namespace='/socketio')

    async def disconnect(sid):
        server_name = server_sid.inv[sid]
        del server_sid[server_name]
        await sio.emit('reply', f'{server_name}已斷線', namespace='/socketio')

    sio = socketio.AsyncServer(async_mode="asgi")
    sio.on("disconnect", disconnect, namespace="/socketio")
    sio.on("chat message", message, namespace="/socketio")
    sio.on("connect", connect, namespace="/socketio")
    app.mount("/", socketio.ASGIApp(socketio_server=sio))
    logger.info("socketio init")

