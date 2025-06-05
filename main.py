import os
from openweather_data import fetch_weather
from dotenv import load_dotenv
from excel import save_to_excel
load_dotenv()

api_key = os.getenv("OPENWEATHER_KEY")
api_city = os.getenv("OPENWEATHER_CITY")

weather_result = fetch_weather(api_key, api_city)
# zapisz pobrane dane do excela excel(dane)
save_to_excel(weather_result)