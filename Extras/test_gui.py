from tkinter import *
from tkinter.messagebox import *

class Tester:
    def __init__(self):
        self.root = Tk()

        self.mult_var = IntVar()

        self.rb1 = Radiobutton(self.root, text="x5", variable=self.mult_var, value=5)
        self.rb2 = Radiobutton(self.root, text="x10", variable=self.mult_var, value=10)
        self.rb3 = Radiobutton(self.root, text="x15", variable=self.mult_var, value=15)

