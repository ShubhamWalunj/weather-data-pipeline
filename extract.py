import requests
import json

# We use Open-Meteo API because it's free and needs no key!
URL = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=true"

def fetch_weather():
    response = requests.get(URL)
    data = response.json()
    
    # Save the "Bronze" (Raw) data to a JSON file
    with open('raw_weather.json', 'w') as f:
        json.dump(data, f)
    print("Step 1: Raw data extracted and saved!")

fetch_weather()