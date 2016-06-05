#from src.weather import watson_weather_model as weather
from serially_arduino import ArduinoValues
import schedule

class Operations:

    def get_water_restrictions(self):
        schedule.get_if_watering_restriction()

    def get_arduino_values(self):
        ard_values = ArduinoValues()
ard_values = ArduinoValues()
print(ard_values.get_arduino_attr())


