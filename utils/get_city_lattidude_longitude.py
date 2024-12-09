from geopy.geocoders import Nominatim

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None
