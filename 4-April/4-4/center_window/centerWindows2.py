from tkinter import *

def center_window(w=500, h=500):
    # Get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # Calculate x and y for perfect center
    x = (ws - w) // 2
    y = (hs - h) // 2

    # Set the geometry (size + position)
    root.geometry(f'{w}x{h}+{x}+{y}')

root = Tk()
center_window(400, 300)
root.mainloop()
