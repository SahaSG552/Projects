from abc import ABC, abstractmethod


class CallDevice(ABC):
    @abstractmethod
    def call():
        pass
