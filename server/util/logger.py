from loguru import logger
import logging
import requests
import threading
import os

mainlogger = None


def get_logger():
    global mainlogger
    if not mainlogger:
        mainlogger = Logger().get_logger()
    return mainlogger


class Websocket_handler(logging.Handler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def notify(self, message: str):
        def do_request():
            url = os.getenv("KNOWLEDGE_SERVER", "http://localhost:8000")
            requests.post(
                f"{url}/socketio/logger",
                json={"message": message},
            )

        thread = threading.Thread(target=do_request)
        thread.start()

    def emit(self, record: logging.LogRecord) -> None:
        testdata = self.format(record)
        self.notify(testdata)


class Logger:
    def __init__(self):
        self.logger = self.__set_logger()

    def __set_logger(self):
        logger.add(Websocket_handler(), level="INFO")
        return logger

    def __getattr__(self, level: str):
        return getattr(self.logger, level)

    def get_logger(self):
        return self.logger
