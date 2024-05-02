import requests

class WeatherManager():
    def __init__(self, api_key) -> None:
        self.api_key: str = api_key
        self.weather_data: requests.Response
        self.location: str = "Default location"
        self.temperature: float = 0.0
        self.temperature_unit: str = "F"
        self.windspeed: float = 0.0
        self.wind_unit: str = "mph"
        self.humidity: float = 0
        self.condition: str = "Default weather condition"

    def __str__(self):
        return (
            f"Weather in {self.location}:\n"
            f"Temperature: {self.temperature}°{self.temperature_unit}\n"
            f"Windspeed: {self.windspeed} {self.wind_unit}\n"
            f"Humidity: {self.humidity}%\n"
            f"Condition: {self.condition}\n"
        )

    def getData(self, location: str):
        # Set location
        self.location = location

        # Request with location and api. Returns JSON
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.location}&units=imperial&APPID={self.api_key}")
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            self.weather_data = response.json()  # Assign only if response is successful
            print(f"Weather data retrieved successfully. Status code: {response.status_code}")
            print(self.weather_data)
            # Update information
            self.parse_temperature()
            self.parse_windspeed()
            self.parse_location()
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

    # Parses data from self.weather_data and updates self.location
    def parse_location(self):
        if 'name' in self.weather_data:
            self.location = self.weather_data['name']
        else:
            print("Location data not available.")
    
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

    def convertTemperature(self):
        """
        Converts self.temperature between 
        Celcius and Farenheit depending on self.temperature_unit.
        """

        if self.temperature_unit == "F":
            self.temperature = round((self.temperature - 32) * 5 / 9) # Conversion formula
            self.temperature_unit = "C"
        else:
            self.temperature = round(self.temperature * 9 / 5 + 32)
            self.temperature_unit = "F"
        print(f"Temperature converted to { self.temperature_unit }: { self.temperature }")

    def convertWindspeed(self):
        """
        Converts self.windspeed between 
        mph and km/h depending on self.wind_unit.
        """

        if self.wind_unit == "mph":
            self.windspeed = round(self.windspeed * 1.60934) # Constant used in conversion formula
            self.wind_unit = "km/h"
        else:
            self.windspeed = round(self.windspeed / 1.60934)
            self.wind_unit = "mph"
        print(f"Windspeed converted to { self.wind_unit }: { self.windspeed }")
