from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("light")

class WeatherApp(ctk.CTk):
    """Displays the main application window"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("970x650")
        self.resizable(False, False)
        self.title("Tempest Tracker")
        
        self.background_img = ImageTk.PhotoImage(Image.open("images/bkgrnd.jpg"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack()

        '''
            LIST OF WIDGETS TO BE CREATED:

            searchBox (input field)
            searchButton (button)
            refreshButton (button)

            locationLabel (dynamic & static label)
            temperatureLabel (dynamic & static label)
            windSpeedLabel (dynamic & static label)
            humidityLabel (dynamic & static label)
            conditionLabel (dynamic & static label)

            LESS IMPORTANT WIDGETS:
            temperatureSwitch (f to c)
            windSpeedSwitch (f to c)
        ''' 


        
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()