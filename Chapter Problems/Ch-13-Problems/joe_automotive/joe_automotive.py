# Programmer: Mason Colacicco
# Date: April
# Program: Joe's Automotive

from tkinter import *
from tkinter.messagebox import *


class AutomotiveGUI:
    def __init__(self):
        # Create window
        self.root = Tk()

        # Create frames
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)

        # Create the dictionary for the checkboxes
        self.services = {'Oil change': (IntVar(), 30),
                         'Lube job': (IntVar(), 20),
                         'Radiator flush': (IntVar(), 40),
                         'Transmission flush': (IntVar(), 100),
                         'Inspection': (IntVar(), 35),
                         'Muffler replacement': (IntVar(), 200),
                         'Tire rotation': (IntVar(), 20)}

        # Create checkbuttons and pack
        for service, (var, price) in self.services.items():
            self.check = Checkbutton(self.top_frame, text=service, variable=var, onvalue=price, offvalue=0)
            self.check.pack()

        # Create calc and quit
        self.calc_button = Button(self.bottom_frame, text='Calculate', command=self.calc)
        self.quit_button = Button(self.bottom_frame, text='Quit', command=self.root.destroy)

        # Pack buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack Frames
        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')

        # window loop
        self.root.mainloop()

    def calc(self):
        # Make total by going through each var
        total = sum(var.get() for var, price in self.services.values())
        showinfo('Final Total',
                 f'Final Total = ${total:,.2f}')


if __name__ == '__main__':
    automotive = AutomotiveGUI()
