'''
# It is included in the main.p

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

        # Search Box
        #self.searchBox = ctk.CTkEntry(self, placeholder_text="CTkEntry")
        self.textbox = ctk.CTkTextbox(self.background_label, activate_scrollbars=False, width=150, height=15, corner_radius=0)
        self.textbox.pack()

        # Search Button
        self.searchButton = ctk.CTkButton(self.background_label, text="Search", width=110, corner_radius=6,
                                         font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                         hover_color="gray", text_color="white", command=self.sayHi)
        self.searchButton.pack()

    def sayHi(self):
        print("button pressed")
        
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()


    # Sharing screen

'''

