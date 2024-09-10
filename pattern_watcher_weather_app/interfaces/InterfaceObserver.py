from abc import ABC, abstractmethod


class InterfaceObserver(ABC):
    @abstractmethod
    def update(self): ...
