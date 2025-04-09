# Programmer: Mason Colacicco
# Date: April
# Program: Updated GUI

import tkinter


class MyGUI:
    def __init__(self):
        # Create main window widget
        self.main_window = tkinter.Tk()

        # Create two frames, one at top of window and one at the bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create three label widgets for the top frame
        self.label1 = tkinter.Label(self.top_frame, text="Minnesota")
        self.label2 = tkinter.Label(self.top_frame, text="Iowa")
        self.label3 = tkinter.Label(self.top_frame, text="Wisconsin")

        # Pack the top_frame labels
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Create three label widgets for the bottom frame
        self.label4 = tkinter.Label(self.bottom_frame, text="St Paul")
        self.label5 = tkinter.Label(self.bottom_frame, text="Des Moines")
        self.label6 = tkinter.Label(self.bottom_frame, text="Madison")

        # Pack the top_frame labels
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the main loop
        tkinter.mainloop()


# Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
