



weather_conditions = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Foggy",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Light snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorms",
    96: "Thunderstorms with hail",
    99: "Thunderstorms with heavy hail"
}






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
        85: snow, # TODO: to change
        86: snow,
        95: sun,
        96: sun,
        99: sun
    }

    return weather_conditions_images.get(int(weather_code), sun)