import requests
from datetime import datetime
from tools import convert_to_celsius

def fetch_weather(key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(url)

    # Odczytuje JSON i sprowadza go do formy bardzo zbliżonej do dict
    data = response.json()

    weather = {
        "datetime": datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
        "temperature": convert_to_celsius(data['main']['temp']),
        "perc_temp": convert_to_celsius(data['main']['feels_like']),
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed'],
        "city": data['name']
    }
    return weather

