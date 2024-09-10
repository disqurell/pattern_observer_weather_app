import time

from WeatherData import WeatherData

from CurrentConditionsDisplay import CurrentConditionsDisplay
from ForecastDisplay import ForecastDisplay


class WeatherStation:
    def __init__(self) -> None:
        self.weatherData = WeatherData()

    def test_1(self):
        currentConditionDisplay = CurrentConditionsDisplay(self.weatherData)
        forecastDisplay = ForecastDisplay(self.weatherData)

        self.weatherData.setMeasurements(20, 20, 600)

        time.sleep(2)

        self.weatherData.setMeasurements(50, 10, 45)

    def run(self):
        self.test_1()


WeatherStation().run()
