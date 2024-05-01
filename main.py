# API Imports
import requests
from weather_manager import WeatherManager
from config import api_key

# Tkinter Imports
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
ctk.set_appearance_mode("light")

# Instantiate WeatherManager
weather_manager = WeatherManager(api_key)

class WeatherApp(ctk.CTk):
    """Displays the main application window"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("970x650")
        self.resizable(False, False)
        self.title("Tempest Tracker")
        
        self.background_img = ImageTk.PhotoImage(Image.open("images/bkgrnd.jpg"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack(expand=True, fill="both")

        # Search Box

        #self.searchBox = ctk.CTkEntry(self, placeholder_text="CTkEntry")
        self.textbox = ctk.CTkTextbox(self.background_label, activate_scrollbars=False, width=150, height=15, corner_radius=0)
        self.textbox.pack()

        # Search Button

        self.searchButton = ctk.CTkButton(self.background_label, text="Search", width=110, corner_radius=6,
                                         font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                         hover_color="gray", text_color="white", command=self.updateWeather)
        self.searchButton.pack()

         # Refresh Button

        self.refreshButton = ctk.CTkButton(self.background_label, text="Refresh", width=110, corner_radius=6,
                                         font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                         hover_color="gray", text_color="white", command=self.updateWeather)
        self.refreshButton.pack()

        # Temperature Label

        self.temperatureLabel = ctk.CTkLabel(self.background_label, text="Temperature", font=ctk.CTkFont("Arial", size=22))
        self.temperatureLabel.pack()

        # Windspeed Label

        self.windspeedLabel = ctk.CTkLabel(self.background_label, text="Windspeed", font=ctk.CTkFont("Arial", size=22))
        self.windspeedLabel.pack()

        # Humidity Label

        self.humidityLabel = ctk.CTkLabel(self.background_label, text="Humidity", font=ctk.CTkFont("Arial", size=22))
        self.humidityLabel.pack()

        # Condition Label

        self.conditionLabel = ctk.CTkLabel(self.background_label, text="Condition", font=ctk.CTkFont("Arial", size=22))
        self.conditionLabel.pack()

    def updateWeather(self):
        user_input = self.textbox.get(1.0, END)  # Retrieve text from the beginning to the end
        weather_manager.getData(user_input)
        print(weather_manager)

        # Update all labels (When the Refresh Button is Pressed)

        self.updateTemperature()
        self.updateWindspeed()
        self.updateHumidity()
        self.updateCondition()

    def updateTemperature(self):
        self.temperatureLabel.configure(text=f"Temp: {weather_manager.temperature}°F")

    def updateWindspeed(self):
        self.windspeedLabel.configure(text=f"Windspeed: {weather_manager.windspeed}mph")

    def updateHumidity(self):
        self.humidityLabel.configure(text=f"Humidity: {weather_manager.humidity}°%")

    def updateCondition(self):
        self.conditionLabel.configure(text=f"Condition: {weather_manager.condition}")
        
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()

'''
    - searchBox (input field)
    - searchButton (button)
    - refreshButton (button)

    - locationLabel (dynamic & static label)
    - temperatureLabel (dynamic & static label)
    - windSpeedLabel (dynamic & static label)
    - humidityLabel (dynamic & static label)
    - conditionLabel (dynamic & static label)
'''