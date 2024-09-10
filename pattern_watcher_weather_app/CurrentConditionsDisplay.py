from WeatherData import WeatherData

from interfaces.InterfaceObserver import InterfaceObserver
from interfaces.InterfaceDisplayElement import InterfaceDisplayElement


class CurrentConditionsDisplay(InterfaceObserver, InterfaceDisplayElement):
    def __init__(self, weatherData: WeatherData) -> None:
        self._weather_data = weatherData
        self._weather_data.registerObserver(self)

        self._temperature = None
        self._humidity = None
        self._pressure = None

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        self.display()

    def display(self):
        print(
            f"Current temperature: {self._temperature}°C, Humidity: {self._humidity}%."
        )
