from interfaces.InterfaceSubject import InterfaceSubject
from interfaces.InterfaceObserver import InterfaceObserver
from typing import List


class WeatherData(InterfaceSubject):
    def __init__(self) -> None:
        super().__init__()

        self._observers: List[InterfaceObserver] = []

        self._temperature: float
        self._humidity: float
        self._pressure: float

    def registerObserver(self, observer: InterfaceObserver):
        self._observers.append(observer)

    def removeObserver(self, observer: InterfaceObserver):
        self._observers.remove(observer)

    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        self.notifyObservers()
