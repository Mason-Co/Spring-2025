# Programmer: Mason Colacicco
# Date: April
# Program: Long Distance Calls

from tkinter import *
from tkinter.messagebox import *

class LongDistance:
    def __init__(self):
        # Create main window
        self.window = Tk()

        # Create frames
        self.top_frame = Frame(self.window)
        self.mid_frame = Frame(self.window)
        self.bot_frame = Frame(self.window)

        # Create Variables
        self.minutes = IntVar()
        self.rb_var = IntVar()

        # Set var to 1
        self.rb_var.set(1)

        # Create radiobuttons
        self.rb1 = Radiobutton(self.top_frame, text='Daytime (6:00 am - 5:59 pm)', variable=self.rb_var, value=1)
        self.rb2 = Radiobutton(self.top_frame, text='Evening (6:00 pm - 11:59 pm)', variable=self.rb_var, value=2)
        self.rb3 = Radiobutton(self.top_frame, text='Off-Peak (12:00 am - 5:59 am)', variable=self.rb_var, value=3)

        # pack the radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create label and entry
        self.min_label = Label(self.top_frame, text='Minutes:')
        self.min_entry = Entry(self.mid_frame)

        # Pack entry
        self.min_label.pack(side='left')
        self.min_entry.pack(side='left')

        # Create buttons
        self.display_button = Button(self.bot_frame, text='Display Charges', command=self.calculate)
        self.quit_button = Button(self.bot_frame, text='Quit', command=self.window.destroy)

        # Pack buttons
        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        # Create main loop
        self.window.mainloop()

    def calculate(self):
        self.minutes = self.min_entry.get()

        if self.rb_var.get() == 1:
            rate = 0.10
        elif self.rb_var.get() == 2:
            rate = 0.15
        else:
            rate = 0.05

        # Calculate
        charges = float(self.minutes) * rate

        showinfo('Total Charges',
                 f'Your total charges = ${charges:,.2f}')

if __name__ == '__main__':
    long_dist = LongDistance()