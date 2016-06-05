#from src.weather import watson_weather_model as weather
from serially_arduino import ArduinoValues
import schedule

class Operations:

    def get_water_restrictions(self):
        restrictions = schedule.get_if_watering_restriction()
        return restrictions

    def get_arduino_values(self):
        a = ArduinoValues()
        return a.get_all()


