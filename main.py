# Standard library imports
import requests

# Third-party library imports
from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
# import pywinstyles

# Local imports
from weather_manager import WeatherManager
from utility import _from_rgb
from config import api_key

# Constants
BACKGROUND_IMAGE_PATH = "images/background_image.jpg"
REFRESH_IMAGE_PATH = "images/refresh.png"
SEARCH_IMAGE_PATH = "images/search.png"
MAIN_FRAME_WIDTH = 850
MAIN_FRAME_HEIGHT = 450

class WeatherApp(ctk.CTk):
    """Displays the main application window"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("970x650")
        self.resizable(False, False)
        self.title("Tempest Tracker")
        
        # Load background image
        self.background_img = ImageTk.PhotoImage(Image.open(BACKGROUND_IMAGE_PATH))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack(expand=True, fill="both")
        
        # Set appearance mode
        ctk.set_appearance_mode("light")

        # Instantiate WeatherManager
        self.weather_manager = WeatherManager(api_key)

        # Create main frame with transparent corners
        self.create_main_frame()
        self.create_widgets()

    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(self, width=MAIN_FRAME_WIDTH, height=MAIN_FRAME_HEIGHT, fg_color="#257281", bg_color="#FFFFFF", corner_radius=30)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        #pywinstyles.set_opacity(self.main_frame, color="#000001", value=0.7)

    def create_widgets(self):
        "Create an entry widget for user input"
        self.weather_entry = ctk.CTkEntry(self.main_frame, width=550, height=50, fg_color="white",
                                           bg_color="#257281", placeholder_text="Type the location here...", 
                                           placeholder_text_color="black", corner_radius=30,
                                           font=ctk.CTkFont("Arial", size=20, slant="italic"), text_color="black",
                                           border_color="black")
        self.weather_entry.place(x=150, y=100)
        
        "Create a search and refresh button"
        self.search_img = ImageTk.PhotoImage(Image.open(SEARCH_IMAGE_PATH).resize((18, 18)))
        self.search_button = self.create_button(self.weather_entry, "Search", self.search_img, self.updateWeather, 280, 10)
        self.refresh_img = ImageTk.PhotoImage(Image.open(REFRESH_IMAGE_PATH).resize((18, 18)))
        self.refresh_button = self.create_button(self.weather_entry, "Refresh", self.refresh_img, self.update_info_labels, 400, 10)
        
        "Data frame within main frame that contains widgets"
        self.data_frame = ctk.CTkFrame(self.main_frame, width=720, height=200,
                                       fg_color="white", bg_color="#257281", 
                                       border_color="black", border_width=2, corner_radius=30)
        self.data_frame.place(x=70, y=200)
        
        "Labels for weather data"
        self.temp_heading = self.create_heading_label(self.data_frame, "Temperature", 180, 15)
        self.temp_result = self.create_info_label(self.data_frame, f"{self.weather_manager.temperature}{self.weather_manager.temperature_unit}", 180, 40)
        
        "Switch for changing the temperature display unit"
        self.switch_var = ctk.StringVar(value="on")
        self.temp_switch = ctk.CTkSwitch(self.data_frame, text="", width=25,
                                         progress_color="black",
                                         hover=False, button_color=_from_rgb((220,220,220)),
                                         variable=self.switch_var, onvalue="off", offvalue="on", 
                                         command=self.toggle_temperature)
        self.temp_switch.place(x=300, y=18)
        
        "Headings and Labels for Wind Speed"
        self.wind_heading = self.create_heading_label(self.data_frame, "Wind Speed", 400, 15)
        self.wind_result = self.create_info_label(self.data_frame, f"{self.weather_manager.windspeed}{self.weather_manager.wind_unit}", 400, 40)
        
        "Switch for changing the wind speed display unit"
        self.switch_var = ctk.StringVar(value="on")
        self.wind_switch = ctk.CTkSwitch(self.data_frame, text="", width=25,
                                         progress_color="black",
                                         hover=False, button_color=_from_rgb((220,220,220)),
                                         variable=self.switch_var, onvalue="off", offvalue="on", 
                                         command=self.toggle_windspeed)
        self.wind_switch.place(x=520, y=18)

        "Headings and Labels for Current Location"
        self.location_heading = self.create_heading_label(self.data_frame, "Location", 90, 90)
        self.location_result = self.create_info_label(self.data_frame, f"{self.weather_manager.location}", 90, 115)

        "Headings and Labels for Humidity"
        self.humidity_heading = self.create_heading_label(self.data_frame, "Humidity", 310, 90)
        self.humidity_result = self.create_info_label(self.data_frame, f"{self.weather_manager.humidity}%", 310, 115)

        "Headings and Labels for Weather Condition"
        self.condition_heading = self.create_heading_label(self.data_frame, "Condition", 510, 90)
        self.condition_result = self.create_info_label(self.data_frame, f"{self.weather_manager.condition}", 510, 115)

    def create_heading_label(self, parent, text, x, y):
        """
        Single method used for header creation 
        so all headers have the same styling

        Args:
            parent (ctkWidget): Parent display object
            text (str): Text displayed on the label
            x (int): x position on screen
            y (int ): y position on screen

        Returns:
            label (ctk.CTkLabel): The header label object
        """        
        label = ctk.CTkLabel(parent, text=text,
                            font=ctk.CTkFont("Arial", size=18),
                            text_color="#949494")
        label.place(x=x, y=y)
        return label
    
    def create_info_label(self, parent, text, x, y):
        """
        Single method used for creating info labels
        so all info labels have the same styling

        Args:
            parent (ctkWidget): Parent display object
            text (str): Text displayed on the label
            x (int): x position on screen
            y (int ): y position on screen

        Returns:
            label (ctk.CTkLabel): The info label object
        """ 
        label = ctk.CTkLabel(parent, text=text,
                            font=ctk.CTkFont("Arial", size=18),
                            text_color="black")
        label.place(x=x, y=y)
        return label


    def create_button(self, parent, text, image, command, x, y):
        """
        Single method used for button creation
        so all buttons have the same styling

        Args:
            parent (ctkWidget): Parent display object
            text (str): Text displayed on the button
            image (ctkImage): Image displayed by the text
            command (function): Function called on button press
            x (int): x position on screen
            y (int ): y position on screen

        Returns:
            button (ctk.CTkButton): The button object
        """            
        button = ctk.CTkButton(parent, image=image, text=text, width=100, anchor="center",
                            font=ctk.CTkFont("Arial", size=16),
                            fg_color="#3ba1c8", bg_color="#FFFFFF", corner_radius=20,
                            hover_color="gray", command=command)
        button.place(x=x, y=y)
        #pywinstyles.set_opacity(button, color="#000001", value=1)
        return button

    def updateWeather(self):
        """
        This method gets user input from the entry box
        and makes an API call thorugh weather_manager.getData()
        Then the info labels display the resulting data.
        """        
        user_input = self.weather_entry.get()  # Retrieve text from the beginning to the end
        print(f"USER_INPUT: {user_input}")
        self.weather_manager.getData(user_input)
        print(self.weather_manager)

        self.update_info_labels()

    def toggle_temperature(self):
        self.weather_manager.convertTemperature()
        self.update_info_labels()

    def toggle_windspeed(self):
        self.weather_manager.convertWindspeed()
        self.update_info_labels()

    def update_info_labels(self):
        # Update all labels (When the Refresh Button is Pressed)
        self.temp_result.configure(text=f"{self.weather_manager.temperature}°{self.weather_manager.temperature_unit}")
        self.wind_result.configure(text=f"{self.weather_manager.windspeed}{self.weather_manager.wind_unit}")
        self.location_result.configure(text=f"{self.weather_manager.location}")
        self.humidity_result.configure(text=f"{self.weather_manager.humidity}%")
        self.condition_result.configure(text=f"{self.weather_manager.condition}")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()