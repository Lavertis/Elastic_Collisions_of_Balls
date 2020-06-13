import locale
from tkinter import *


class Controls:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')
        self.window = Tk()
        window_size = str(round(self.window.winfo_screenwidth() * 0.13)) + 'x' + str(
            round(self.window.winfo_screenheight() * 0.48)) + '+' + str(
            round(self.window.winfo_screenwidth() * 0.75)) + '+' + str(
            round(self.window.winfo_screenheight() * 0.2))
        self.window.geometry(window_size)
        self.window.resizable(0, 0)
        self.window.attributes('-topmost', True)
        self.window.title("Balls")
        self.number_label = Label(self.window, text="\nNumber", font=("Courier", 14))
        self.number_label.pack()
        self.number_scale = Scale(self.window, length=200, width=25, sliderlength=50, from_=1, to=100,
                                  orient=HORIZONTAL)
        self.number_scale.pack()
        self.velocity_label = Label(self.window, text="\nVelocity", font=("Courier", 14))
        self.velocity_label.pack()
        self.velocity_scale = Scale(self.window, length=200, width=25, sliderlength=50, from_=0.1, to=10,
                                    resolution=0.1, orient=HORIZONTAL)
        self.velocity_scale.pack()
        self.radius_label = Label(self.window, text="\nRadius", font=("Courier", 14))
        self.radius_label.pack()
        self.radius_scale = Scale(self.window, length=200, width=25, sliderlength=50, from_=1, to=50, orient=HORIZONTAL)
        self.radius_scale.pack()
        self.colour_label = Label(self.window, text="\nColour", font=("Courier", 14))
        self.colour_label.pack()
        self.colour_scale = Scale(self.window, length=200, width=25, sliderlength=50, from_=1, to=6, resolution=1,
                                  orient=HORIZONTAL)
        self.colour_scale.pack()
        self.space_label = Label(self.window, text='\n')
        self.space_label.pack()
        self.reset_button = Button(self.window, text="Reset", height=1, width=11, font=("Courier", 14))
        self.reset_button.pack()
