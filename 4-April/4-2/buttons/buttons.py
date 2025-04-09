# Programmer: Mason Colacicco
# Date: April
# Program: Buttons
import tkinter


class ShowInfoGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create two frames, one at top of window and one at the bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create blank label at the top of the frame
        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame, textvariable=self.value)

        # Create two buttons at bottom of frame
        self.address_button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the label
        self.address_label.pack()
        # Pack the buttons
        self.address_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    def show_info(self):
        self.value.set('Mason Colacicco\n 10338 Major Dr N\nBrooklyn Park, MN 55443')


if __name__ == '__main__':
    show_info = ShowInfoGUI()
