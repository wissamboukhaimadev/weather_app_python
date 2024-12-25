import requests
from datetime import datetime, timedelta



url = "https://archive-api.open-meteo.com/v1/archive"

def get_data_city_history(latitude, longitude):

    current_date=datetime.now().date() - timedelta(days=1)
    last_week_date = current_date - timedelta(days=6)

    
    parametres = {
        "latitude": latitude,  
        "longitude": longitude,  
        "start_date": last_week_date,
	    "end_date": current_date,
	    "daily": ["weather_code","temperature_2m_max", "temperature_2m_mean", "precipitation_sum", "rain_sum", "wind_speed_10m_max"]
    }
    reponse = requests.get(url, params=parametres)
    data = reponse.json()

    
    data_time = data['daily']['time']
    data_weather_code = data['daily']['weather_code']
    data_temperature_max = data['daily']['temperature_2m_max']
    data_temperature_mean = data['daily']['temperature_2m_mean']
    data_precipitation_sum = data['daily']['precipitation_sum']
    data_rain_sum = data['daily']['rain_sum']
    data_wind_speed_10m_max = data['daily']['wind_speed_10m_max']

    return data_time, data_weather_code, data_temperature_max, data_temperature_mean, data_precipitation_sum, data_rain_sum, data_wind_speed_10m_max