import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("My first GUI")

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()