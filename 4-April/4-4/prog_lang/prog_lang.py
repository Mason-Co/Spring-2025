# Programmer: Mason Colacicco
# Date: April
# Program: Programming Languages Algorithm

from tkinter import *
from tkinter.messagebox import *

class ListboxLang:
    def __init__(self):
        # Create Window and title
        self.main_window = Tk()
        self.main_window.title('Programming Languages')

        # Get screen width and height
        ws = self.main_window.winfo_screenwidth()
        hs = self.main_window.winfo_screenheight()

        # Set height and width
        w = 200
        h = 175

        # Calculate x and y for perfect center
        x = (ws - w) // 2
        y = (hs - h) // 2

        # Set the geometry (size + position)
        self.main_window.geometry(f'{w}x{h}+{x}+{y}')

        # Create frames
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        # Create Listbox
        self.lang_list = Listbox(self.top_frame, width=0, height=0)
        self.lang_list.pack(padx=5, pady=5)

        # Populate List
        self.lang_list.insert(0,'C')
        self.lang_list.insert(1,'C++')
        self.lang_list.insert(2,'Java')
        self.lang_list.insert(3,'Python')
        self.lang_list.insert(4,'JavaScript')
        self.lang_list.insert(5,'C#')

        # Create Buttons
        self.printBtn = Button(self.bottom_frame, text="Print", command=self.printItem)
        self.delBtn = Button(self.bottom_frame, text="Delete", command=self.delItem)
        self.quitBtn = Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack buttons
        self.printBtn.pack(side='left')
        self.delBtn.pack(side='left')
        self.quitBtn.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Create main loop
        self.main_window.mainloop()

    # Create the print button function
    def printItem(self):
        indexes = self.lang_list.curselection()
        if len(indexes) > 0:
            showinfo(message=self.lang_list.get(indexes[0]))
        else:
            showinfo(message='No item selected.')

    # Create the delete button function
    def delItem(self):
        indexes = self.lang_list.curselection()
        if len(indexes) > 0:
            for i in indexes:
                self.lang_list.delete(i)
                print("One item deleted")
        else:
            showinfo(message='No item selected.')

# GUI if main
if __name__ == '__main__':
    listbox_language = ListboxLang()