import os
import time
from openweather_data import fetch_weather
from dotenv import load_dotenv
from excel import save_to_excel
load_dotenv()

api_key = os.getenv("OPENWEATHER_KEY")
api_city = os.getenv("OPENWEATHER_CITY")
excel_path = os.getenv("EXCEL_FILE_PATH")
interval = float(os.getenv("CRON_INTERVAL"))

while True:
    weather_result = fetch_weather(api_key, api_city)
    # zapisz pobrane dane do excela excel(dane)
    save_to_excel(weather_result, excel_path)
    print(f"Zapisano dane {weather_result['datetime']}")
    time.sleep(interval)
