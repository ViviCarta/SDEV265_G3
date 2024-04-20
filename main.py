# Library for general API requests
import requests
# Import API key from config
from config import api_key



# Get user input
user_input = input("Enter location: ")

# Make request using location
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# 200 = succesfull, 404 = request failed
print(weather_data.status_code)

# Returns all, unparsed data in json format
print(weather_data.json())



# Validates output
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    # Manually parsing weather and temp data
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    # Display information
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")