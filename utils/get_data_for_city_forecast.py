import requests
import json
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim



url = "https://api.open-meteo.com/v1/forecast"

def get_data_city_forecast(latitude, longitude, past_days):

    current_date=datetime.now().date() - timedelta(days=1)
    last_week_date = current_date - timedelta(days=6)


    
    parametres = {
        "latitude": latitude,  
        "longitude": longitude,  
        "pastdays": past_days,
	    "daily": ["weather_code", "temperature_2m_max"]
    }
    reponse = requests.get(url, params=parametres)
    data = reponse.json()
    
    
    data_time = data['daily']['time']
    data_weather_code = data['daily']['weather_code']
    data_temperature_max = data['daily']['temperature_2m_max']

    return data_time, data_weather_code, data_temperature_max





