from abc import ABC, abstractmethod


class BasicChat(ABC):
    @abstractmethod
    def ASK(self, question: str):
        return NotImplemented
