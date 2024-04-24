import requests

class WeatherManager():
    def __init__(self, api_key) -> None:
        self.api_key: str = api_key
        self.weather_data: requests.Response
        self.city: str = "Default city"
        self.temperature: float = 0.0
        self.windspeed: float = 0.0
        self.humidity: float = 0
        self.condition: str = "Default weather condition"

    def __str__(self):
        return (
            f"Weather in {self.city}:\n"
            f"Temperature: {self.temperature}°F\n"
            f"Windspeed: {self.windspeed} mph\n"
            f"Humidity: {self.humidity}%\n"
            f"Condition: {self.condition}\n"
        )

    def getData(self, city: str):
        # Set city
        self.city = city

        # Request with city and api. Returns JSON
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&units=imperial&APPID={self.api_key}")
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            self.weather_data = response.json()  # Assign only if response is successful
            print(f"Weather data retrieved successfully. Status code: {response.status_code}")
            # Update information
            self.parse_temperature()
            self.parse_windspeed()
            self.parse_humidity()
            self.parse_condition()
        else:
            print(f"Failed to retrieve weather data. Status code: {response.status_code}")

    # Parses data from self.weather_data and updates self.temperature
    def parse_temperature(self):
        if 'main' in self.weather_data and 'temp' in self.weather_data['main']:
            self.temperature = self.weather_data['main']['temp']
        else:
            print("Temperature data not available.")

    # Parses data from self.weather_data and updates self.windspeed
    def parse_windspeed(self):
        if 'wind' in self.weather_data and 'speed' in self.weather_data['wind']:
            self.windspeed = self.weather_data['wind']['speed']
        else:
            print("Wind speed data not available.")

    # Parses data from self.weather_data and updates self.humidity
    def parse_humidity(self):
        if 'main' in self.weather_data and 'humidity' in self.weather_data['main']:
            self.humidity = self.weather_data['main']['humidity']
        else:
            print("Humidity data not available.")

    # Parses data from self.weather_data and updates self.condition
    def parse_condition(self):
        if 'weather' in self.weather_data and len(self.weather_data['weather']) > 0 and 'main' in self.weather_data['weather'][0]:
            self.condition = self.weather_data['weather'][0]['main']
        else:
            print("Weather condition data not available.")