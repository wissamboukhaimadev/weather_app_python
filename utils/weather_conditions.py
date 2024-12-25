def get_weathercode_icon(weather_code, clear_sky, moon, partly_cloudy, overcast, foggy, drizzle, cloud, freezing_rain, snow, shower, sun):
    weather_conditions_images = {
        0: clear_sky,
        1: moon,
        2: partly_cloudy,
        3: overcast,
        45: foggy,
        48: foggy,
        51: drizzle,
        53: drizzle,
        55: drizzle,
        61: cloud,
        63: cloud,
        65: cloud,
        66: freezing_rain,
        67: freezing_rain,
        71: snow,
        73: snow,
        75: snow,
        77: snow,
        80: shower,
        81: shower,
        82: shower,
        85: snow, 
        86: snow,
        95: sun,
        96: sun,
        99: sun
    }

    return weather_conditions_images.get(int(weather_code), sun)