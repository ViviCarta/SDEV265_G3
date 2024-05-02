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
        
        "Create a main frame to hold widgets"
        self.main_frame = ctk.CTkFrame(self.background_label, width=850, height=450,
                                       fg_color="#257281", bg_color="#deccb9", corner_radius=30)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        "Create an entry widget for user input"
        self.weather_entry = ctk.CTkEntry(self.main_frame, width=550, height=50, fg_color="white",
                                           bg_color="#257281", placeholder_text="Type the location here...", 
                                           placeholder_text_color="black", corner_radius=30,
                                           font=ctk.CTkFont("Arial", size=20, slant="italic"), text_color="black",
                                           border_color="black")
        self.weather_entry.place(x=150, y=100)
        
        "Create a search button"
        self.search_button = ctk.CTkButton(self, text="Search", width=100, anchor="center",
                                           font=ctk.CTkFont("Arial", size=16),
                                           fg_color="#3ba1c8", bg_color="white", corner_radius=20,
                                           hover_color="gray", command=self.updateWeather)
        self.search_button.place(x=500, y=210)
        
        "Create a refresh button"
        self.refresh_button = ctk.CTkButton(self, text="Refresh", width=100, anchor="center",
                                           font=ctk.CTkFont("Arial", size=16),
                                           fg_color="#3ba1c8", bg_color="white", corner_radius=20,
                                           hover_color="gray", command=self.updateWeather)
        self.refresh_button.place(x=620, y=210)
        
        "Create a frame within main frame to hold data widgets"
        self.data_frame = ctk.CTkFrame(self.main_frame, width=720, height=200,
                                       fg_color="white", bg_color="#257281", 
                                       border_color="black", border_width=2, corner_radius=30)
        self.data_frame.place(x=70, y=200)
        
        "Create heading for Temperature"
        self.temp_heading = ctk.CTkLabel(self.data_frame, text="Temperature",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="#949494")
        self.temp_heading.place(x=180, y=15)
        
        "Create a label that will display Temperature result"
        self.temp_result = ctk.CTkLabel(self.data_frame, text="0.0°F",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="black")
        self.temp_result.place(x=180, y=40)
        
        "Create heading for Wind Speed"
        self.wind_heading = ctk.CTkLabel(self.data_frame, text="Wind Speed",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="#949494")
        self.wind_heading.place(x=400, y=15)
        
        "Create a label that will display Wind Speed result"
        self.wind_result = ctk.CTkLabel(self.data_frame, text="0.0 mph",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="black")
        self.wind_result.place(x=400, y=40)

        "Create heading for Current Location"
        self.location_heading = ctk.CTkLabel(self.data_frame, text="Location",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="#949494")
        self.location_heading.place(x=90, y=90)

        "Create a label that will display Current Location result"
        self.location_result = ctk.CTkLabel(self.data_frame, text="Default Location",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="black")
        self.location_result.place(x=90, y=115)

        "Create heading for Humidity"
        self.humidity_heading = ctk.CTkLabel(self.data_frame, text="Humidity",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="#949494")
        self.humidity_heading.place(x=310, y=90)

        "Create a label that will display Humidity result"
        self.humidity_result = ctk.CTkLabel(self.data_frame, text="0.0%",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="black")
        self.humidity_result.place(x=310, y=115)

        "Create heading for Condition"
        self.condition_heading = ctk.CTkLabel(self.data_frame, text="Condition",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="#949494")
        self.condition_heading.place(x=510, y=90)

        "Create a label that will display Condition result"
        self.condition_result = ctk.CTkLabel(self.data_frame, text="Default condition",
                                        font=ctk.CTkFont("Arial", size=18),
                                        text_color="black")
        self.condition_result.place(x=510, y=115)


    def updateWeather(self):
        user_input = self.weather_entry.get()  # Retrieve text from the beginning to the end
        print(f"USER_INPUT: {user_input}")
        weather_manager.getData(user_input)
        print(weather_manager)

        # Update all labels (When the Refresh Button is Pressed)

        self.updateTemperature()
        self.updateWindspeed()
        self.updateLocation()
        self.updateHumidity()
        self.updateCondition()

    def updateTemperature(self):
        self.temp_result.configure(text=f"{weather_manager.temperature}°{weather_manager.temperature_unit}")

    def updateWindspeed(self):
        self.wind_result.configure(text=f"{weather_manager.windspeed}{weather_manager.wind_unit}")

    def updateLocation(self):
        self.location_result.configure(text=f"{weather_manager.city}")

    def updateHumidity(self):
        self.humidity_result.configure(text=f"{weather_manager.humidity}%")

    def updateCondition(self):
        self.condition_result.configure(text=f"{weather_manager.condition}")
        
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()