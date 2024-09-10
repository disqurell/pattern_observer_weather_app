from abc import ABC, abstractmethod


class InterfaceSubject(ABC):
    @abstractmethod
    def registerObserver(self): ...

    @abstractmethod
    def removeObserver(self): ...

    @abstractmethod
    def notifyObservers(self): ...
