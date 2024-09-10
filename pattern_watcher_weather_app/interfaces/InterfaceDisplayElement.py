from abc import ABC, abstractmethod


class InterfaceDisplayElement(ABC):
    @abstractmethod
    def display(self): ...
