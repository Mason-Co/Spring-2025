# Programmer: Mason Colacicco
# Date: April
# Program: Miles Per Gallon Calculator

import tkinter as tk

class MpgCalculator:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()

        # Create frames
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Create the labels and inputs
        self.miles = tk.IntVar()
        self.gallons = tk.IntVar()
        self.miles_label = tk.Label(self.top_frame, text="Miles")
        self.gallons_label = tk.Label(self.top_frame, text="Gallons")
        self.mpg = tk.StringVar()
        self.mpg_label = tk.Label(self.top_frame, textvariable=self.mpg)

        # Create the entries
        self.miles_entry = tk.Entry(self.top_frame, textvariable=self.miles)
        self.gallons_entry = tk.Entry(self.top_frame, textvariable=self.gallons)

        # Create button
        self.calc_button = tk.Button(self.bottom_frame, text="Calculate", command=self.calculate)

        # Pack labels and entries
        self.miles_label.pack(side='top')
        self.miles_entry.pack(side='top')
        self.gallons_label.pack(side='top')
        self.gallons_entry.pack(side='top')
        self.mpg_label.pack(side='top')

        # Pack buttons
        self.calc_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Create main loop
        self.main_window.mainloop()

    # Create calculate function
    def calculate(self):
        self.mpg.set(f"{self.miles.get() / self.gallons.get():.1f} mpg")

# Display GUI if main
if __name__ == "__main__":
    mpg_GUI = MpgCalculator()