import requests

url = "https://api.open-meteo.com/v1/forecast"

def get_data_city(latitude, longitude):
    parametres = {
        "latitude": latitude,  
        "longitude": longitude,  
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "weather_code"]
    }
    reponse = requests.get(url, params=parametres)
    donnees = reponse.json()

    
    donnees_temperature = donnees['current']['temperature_2m']
    donnees_humidite = donnees['current']['relative_humidity_2m']
    donnees_vitesse_vent = donnees['current']['wind_speed_10m']
    donnees_heure = donnees['current']['time']
    donnees_weather_code = donnees['current']['weather_code']


    return donnees_temperature, donnees_humidite, donnees_vitesse_vent, donnees_heure, donnees_weather_code