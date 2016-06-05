from src.weather import watson_weather_model as weather
from src.weather import geocoding as geocoding
from serially_arduino import ArduinoValues
import schedule

class Operations:

    def get_weather(self):
        address = "St. Edwards University, Austin, TX"

        place = geocoding.get_lat_lon(address)
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

        return current_temp, recent_precip, recent_snow, forecast_min_temp, forecast_max_temp, forecast_precip

    def get_water_restrictions(self):
        restrictions = schedule.get_if_watering_restriction()
        return restrictions

    def get_arduino_values(self):
        a = ArduinoValues()
        return a.get_all()


