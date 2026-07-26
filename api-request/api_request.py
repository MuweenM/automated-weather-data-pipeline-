import os
from pathlib import Path

import requests


def load_env_file():
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        os.environ.setdefault(key, value)


load_env_file()

api_key = os.getenv("WEATHERSTACK_API_KEY", "")
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=Sri Lanka"


def fetch_data():
    print("Fetching weather data from the API...")

    if not api_key:
        raise ValueError("WEATHERSTACK_API_KEY is not set. Add it to the .env file.")

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully.")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise


 


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Colombo, Sri Lanka', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Colombo', 'country': 'Sri Lanka','region': 'Western', 'lat': '6.932', 'lon': '79.848', 'timezone_id': 'Asia/Colombo', 'localtime': '2026-07-26 10:57', 'localtime_epoch': 1785063420, 'utc_offset': '5.50'}, 'current': {'observation_time': '05:27 AM', 'temperature': 29, 'weather_code': 176, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0009_light_rain_showers.png'], 'weather_descriptions': ['Patchy rain nearby'], 'astro': {'sunrise': '06:04 AM', 'sunset': '06:30 PM', 'moonrise': '04:02 PM', 'moonset': '03:05 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 88}, 'air_quality': {'co': '174', 'no2': '6.1', 'o3': '56', 'so2': '6.1', 'pm2_5': '7.5', 'pm10': '12.9', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 19, 'wind_degree': 235, 'wind_dir': 'SW', 'pressure': 1011, 'precip': 0, 'humidity': 75, 'cloudcover': 81, 'feelslike': 33, 'uv_index': 9, 'visibility': 10, 'is_day': 'yes'}}