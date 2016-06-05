from weather import watson_weather_model as weather
from weather import geocoding as geocoding
from serially_arduino import ArduinoValues
from datetime import *
import schedule

class Operations:

    def get_weather(self):
        address = "St. Edwards, 3001 S. Congress, Austin, TX"

        geocode = geocoding.get_geocoding(address)
        place = geocoding.get_lat_lon(geocode)
        latitude = place[u'lat']
        longitude = place[u'lng']

        conditions = weather.get_current_conditions(latitude, longitude)
        current_temp = weather.get_current_temp(conditions)
        recent_precip = weather.get_recent_precipitation(conditions)
        recent_snow = weather.get_recent_snow(conditions)

        forecast = weather.get_forecast(latitude, longitude)
        forecast_precip = weather.get_forecast_precipitation(forecast)
        forecast_min_temp = weather.get_min_forecast_temp(forecast)
        forecast_max_temp = weather.get_max_forecast_temp(forecast)

        return current_temp, recent_precip, forecast_precip

    def get_water_restrictions(self,address_value, property_type):
        restrictions = schedule.get_if_watering_restricted(address=address_value, property_type=property_type, time=datetime.now())
        return restrictions

    def get_arduino_values(self):
        a = ArduinoValues()
        return a.get_all()


