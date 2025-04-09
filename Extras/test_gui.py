from tkinter import *
from tkinter.messagebox import *


class Tester:
    def __init__(self):
        self.root = Tk()
        self.root.title("Test Vending")

        # Var for multiplying vendor items
        self.mult_var = IntVar()

        # Frame for only radios
        self.radio_frame = Frame(self.root)

        # Create radios
        self.mult_var.set(1)
        self.rb1 = Radiobutton(self.radio_frame, text="x1", variable=self.mult_var, value=1)
        self.rb2 = Radiobutton(self.radio_frame, text="x2", variable=self.mult_var, value=2)
        self.rb3 = Radiobutton(self.radio_frame, text="x3", variable=self.mult_var, value=3)

        # Pack radios and its frame
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.radio_frame.grid(row=0, column=0)

        # Frame for checkboxes
        self.check_frame = Frame(self.root)

        # Dictionary for checkboxes
        self.vendors = {'Hot Cheetos': (DoubleVar(), 1.25),
                        'Gushers': (DoubleVar(), 1.25),
                        'Protein Bar': (DoubleVar(), 2.25)}

        # Create checkboxes
        for item, (var, price) in self.vendors.items():
            self.cb = Checkbutton(self.check_frame, text=item, variable=var, onvalue=price, offvalue=0, anchor='w')
            self.cb.pack(fill='x')
        self.check_frame.grid(row=0, column=1)

        # Entry
        self.entry_label = Label(self.root, text="Enter Payment Method: ")
        self.entry_var = StringVar()
        self.entry = Entry(self.root, textvariable=self.entry_var)

        # Pack entry
        self.entry_label.grid(row=1, column=0, pady=5)
        self.entry.grid(row=1, column=1, pady=5)

        # Buttons
        self.show_button = Button(self.root, text="Pay", command=self.calculate)
        self.quit = Button(self.root, text="Quit", command=self.root.destroy)
        self.show_button.grid(row=2, column=0, pady=4)
        self.quit.grid(row=2, column=1, pady=4)

        # Main loop
        self.root.mainloop()

    def calculate(self):
        # Get entry
        payment = self.entry.get()
        # Get radio
        multiplier = self.mult_var.get()
        # Get checks, total
        total = multiplier * sum(var.get() for var, price in self.vendors.values())

        # Messagebox show info
        showinfo('Payment',
                 f'Transaction completed with {payment} for ${total:,.2f}.')


if __name__ == '__main__':
    vendGUI = Tester()
