from abc import ABC, abstractmethod
from typing import List, Dict

#Observer interface
class WeatherObserver(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass
    
class WeatherSubject(ABC):
    @abstractmethod
    def register_observer(self, observer: WeatherObserver) -> None:
        pass
    @abstractmethod
    def remove_observer(self, observer: WeatherObserver) -> None:
        pass
    @abstractmethod
    def notify_observers(self) -> None:
        pass
    

class WeatherStation(WeatherSubject):
    def __init__(self) -> None:
        self._observers: List[WeatherObserver] = []
        self._weather_data: Dict = {"temperature": 0.0, "humidity": 0.0, "pressure": 0.0}
    def register_observer(self, observer: WeatherObserver) -> None:
        self._observers.append(observer)
    
    def remove_observer(self, observer: WeatherObserver) -> None:
        self._observers.remove(observer)
        
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._weather_data["temperature"], self._weather_data["humidity"], self._weather_data["pressure"])
    
    def set_weather_data(self, temperature: float, humidity: float, pressure: float) -> None:
        self._weather_data = {"temperature": temperature, "humidity": humidity, "pressure": pressure}
        self.notify_observers()
        

class CurrentConditionDisplay(WeatherObserver):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Current Condition - Temperature {temperature}, Humidity {humidity}, Pressure {pressure}")

class StatisticsDisplay(WeatherObserver):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Current Condition - Temperature {temperature}, Humidity {humidity}, Pressure {pressure}")
        
class ForecastDisplay(WeatherObserver):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        forecast = "Sunny" if pressure > 1010 else "Rainy"
        print(f"Forecast - Weather is going to be {forecast}")

if __name__ == "__main__":
    weather_station = WeatherStation()
    
    current_conditions_display = CurrentConditionDisplay()        
    statisticsDisplay = StatisticsDisplay()
    forecastDisplay = ForecastDisplay()
    
    weather_station.register_observer(current_conditions_display)
    weather_station.register_observer(statisticsDisplay)
    weather_station.register_observer(forecastDisplay)
    
    print("Weather Update 1:")
    weather_station.set_weather_data(25.6, 65, 1015)
     
