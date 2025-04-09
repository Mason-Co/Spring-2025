# Programmer: Mason Colacicco
# Date: April
# Program: Show Courses
import tkinter


class ShowCoursesGUI:
    def __init__(self):
        # Create window
        self.main_window = tkinter.Tk()

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create label
        self.value = tkinter.StringVar()
        self.courses_label = tkinter.Label(self.top_frame, textvariable=self.value)

        # Create buttons
        self.courses_button = tkinter.Button(self.bottom_frame, text='Show Courses', command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack label
        self.courses_label.pack()
        # Pack buttons
        self.courses_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Create main loop
        tkinter.mainloop()

    # Create show info function
    def show_info(self):
        self.value.set('Data Comm\nDatabase\nPython')

# Run if main
if __name__ == '__main__':
    show_courses_gui = ShowCoursesGUI()