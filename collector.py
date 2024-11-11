from datetime import datetime
from pyowm import OWM
from config import APIKEY

owm = OWM(APIKEY)

def get_observation(zipcode, country):
    manager = owm.weather_manager()
    observation = manager.weather_at_zip_code(zipcode=zipcode, country=country)
    reference_time = datetime.fromtimestamp(observation.reception_time()).strftime('%m/%d/%Y %H:%M:%S')
    return observation, reference_time

def get_current_weather(zipcode, country):
    observation, reference_time = get_observation(zipcode=zipcode, country=country)
    weather = observation.weather
    sunrise = datetime.fromtimestamp(weather.sunrise_time()).strftime('%m/%d/%Y %H:%M:%S')
    sunset = datetime.fromtimestamp(weather.sunset_time()).strftime('%m/%d/%Y %H:%M:%S')
    clouds = weather.clouds
    temperature = weather.temperature('fahrenheit')['temp']
    temp_max = weather.temperature('fahrenheit')['temp_max']
    temp_min = weather.temperature('fahrenheit')['temp_min']
    humidity = weather.humidity
    status = weather.status
    detailed_status = weather.detailed_status
    weather_code = weather.weather_code
    rain1hr = weather.rain.get('1h', 0)
    rain3hr = weather.rain.get('3h', 0)
    snow1hr = weather.snow.get('1h', 0)
    snow3hr = weather.snow.get('3h', 0)
    wind_speed = weather.wind('miles_hour')['speed']
    print(observation.to_dict())