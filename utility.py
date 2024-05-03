from tkinter import messagebox

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def log_error(level: int):
    """Displays an error dialog box based on level"""
    if level == 1:
        messagebox.showerror("Warning", "Did you forget what to input? Do it again!")
    if level == 2:
        messagebox.showerror("Warning", "We know you're a fan of spaces but please change that!")
    elif level == 3:
        messagebox.showerror("Invalid", "Input not recognized by the API. Received 404 error.")