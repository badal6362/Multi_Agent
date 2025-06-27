import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def weather_agent(location_name):
    print(f"\n📍 Weather Agent: Looking up weather for '{location_name}'")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location_name}&appid={OPENWEATHER_API_KEY}&units=metric"
    print(f"➡️  Requesting URL: {url}")

    response = requests.get(url)
    print(f"✅ Status Code: {response.status_code}")

    if response.status_code == 200:
        print("🌤️ Weather data retrieved successfully!\n")
        return response.json()
    else:
        print("❌ Error from weather API:", response.text)
        return {}
