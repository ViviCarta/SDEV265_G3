# Library for general API requests
import requests
# Weather manager
from weather_manager import WeatherManager
# Import API key from config
from config import api_key

# Instantiate WeatherManager
weather_manager = WeatherManager(api_key)

# Get user input
user_input = input("Enter location: ")

weather_manager.getData(user_input)
print(weather_manager)