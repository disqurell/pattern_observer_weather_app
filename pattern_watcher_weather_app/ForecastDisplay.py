from interfaces.InterfaceObserver import InterfaceObserver
from interfaces.InterfaceDisplayElement import InterfaceDisplayElement
from WeatherData import WeatherData


class ForecastDisplay(InterfaceObserver, InterfaceDisplayElement):
    def __init__(self, weatherData: WeatherData) -> None:
        super().__init__()

        self._weather_data = weatherData
        self._weather_data.registerObserver(self)

        self._pressure = None
        self._temperature = None
        self._humidity = None

    def update(self, temperature: float, humidity: float, pressure: float):
        # Обновляем данные
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        # Выводим прогноз на экран
        self.display()

    def display(self):
        forecast = "Forecast: "

        # Прогноз на основе текущих данных температуры, влажности и давления
        if self._pressure is not None:
            if self._pressure < 1000:
                forecast += "Likely rain. "
            elif self._pressure >= 1000 and self._pressure < 1020:
                forecast += "Cloudy, but no rain expected. "
            else:
                forecast += "Clear weather expected. "

            if self._temperature > 25 and self._humidity < 50:
                forecast += "Hot and dry conditions. "
            elif self._temperature < 10:
                forecast += "Cold weather. "
            elif (
                self._temperature >= 10
                and self._temperature <= 25
                and self._humidity > 60
            ):
                forecast += "Mild with possible high humidity. "

        else:
            forecast += "Insufficient data for forecast."

        # Выводим прогноз
        print(forecast)
        print()
