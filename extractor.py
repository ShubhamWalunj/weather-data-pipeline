import requests
import json

class WeatherDataExtractor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.weatherapi.com/v1/'

    def get_weather(self, location):
        url = f'{self.base_url}current.json?key={self.api_key}&q={location}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print('Error fetching data:', response.status_code)
            return None

# Example usage
# extractor = WeatherDataExtractor('your_api_key')
# weather_data = extractor.get_weather('New York')
# print(json.dumps(weather_data, indent=4))