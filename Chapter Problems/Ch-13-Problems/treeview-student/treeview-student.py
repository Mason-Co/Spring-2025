from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('Status Board')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

# scrollbars
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame, orient='horizontal')
game_scroll.pack(side=BOTTOM, fill=X)

# Create table frame
my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

# define our column
my_game['columns'] = ('student_id', 'student_fname', 'student_lname', 'player_Rank')

# Format columns
my_game.column("#0", width=0, stretch=NO)
my_game.column("student_id", anchor=CENTER, width=80)
my_game.column("student_fname", anchor=CENTER, width=80)
my_game.column("student_lname", anchor=CENTER, width=80)
my_game.column("player_Rank", anchor=CENTER, width=80)

# Create Headings
my_game.heading("#0", text="", anchor=CENTER)
my_game.heading("student_id", text="Id", anchor=CENTER)
my_game.heading("student_fname", text="Name", anchor=CENTER)
my_game.heading("student_lname", text="Name", anchor=CENTER)
my_game.heading("player_Rank", text="Rank", anchor=CENTER)

# Insert teams
my_game.insert(parent='', index='end', iid=0, text='',
               values=('1', 'Mason', 'Cola', '3.9'))
my_game.insert(parent='', index='end', iid=1, text='',
               values=('2', 'Mason', 'Pet', '4.0'))
my_game.insert(parent='', index='end', iid=2, text='',
               values=('3', 'Dylan', 'Weak', '4.0'))
my_game.insert(parent='', index='end', iid=3, text='',
               values=('4', 'Breyon', 'G***', '4.0'))
my_game.insert(parent='', index='end', iid=4, text='',
               values=('5', 'Klein', 'Ed', '3.5'))
my_game.insert(parent='', index='end', iid=5, text='',
               values=('6', 'Preston', 'Loe', '3.0'))
my_game.insert(parent='', index='end', iid=6, text='',
               values=('7', 'Trevor', 'Kong', '3.0'))
my_game.insert(parent='', index='end', iid=7, text='',
               values=('8', 'Brock', 'More', '2.5'))
my_game.insert(parent='', index='end', iid=8, text='',
               values=('9', 'Sophia', 'Chris', '3.7'))
my_game.insert(parent='', index='end', iid=9, text='',
               values=('10', 'Josie', 'Mell', '3.8'))
my_game.pack()

frame = Frame(ws)
frame.pack(pady=20)

# Labels
studentid = Label(frame, text="id")
studentid.grid(row=0, column=0)

playerfname = Label(frame, text="First_name")
playerfname.grid(row=0, column=1)

playerlname = Label(frame, text="Last_name")
playerlname.grid(row=0, column=2)

studentGPA = Label(frame, text="GPA")
studentGPA.grid(row=0, column=3)

# Entry boxes: ID, Name, Rank
studentid_entry = Entry(frame)
studentid_entry.grid(row=1, column=0)

studentfname_entry = Entry(frame)
studentfname_entry.grid(row=1, column=1)

studentlname_entry = Entry(frame)
studentlname_entry.grid(row=1, column=2)

studentGPA_entry = Entry(frame)
studentGPA_entry.grid(row=1, column=3)


# Select Record
def select_record():
    # clear entry boxes
    studentid_entry.delete(0, END)
    studentfname_entry.delete(0, END)
    studentlname_entry.delete(0, END)
    studentGPA_entry.delete(0, END)

    # Get row that has focus
    selected = my_game.focus()
    # grab record values
    values = my_game.item(selected, 'values')
    # temp_label.config(text=selected)

    # Insert focus row in entry boxes
    studentid_entry.insert(0, values[0])
    studentfname_entry.insert(0, values[1])
    studentlname_entry.insert(0, values[2])
    studentGPA_entry.insert(0, values[3])

    stuff.set("Record Selected")


# Update Record
def update_record():
    selected = my_game.focus()
    # save new data
    my_game.item(selected, text="", values=(studentid_entry.get(),
                                            studentfname_entry.get(),
                                            studentlname_entry.get(),
                                            studentGPA_entry.get()))

    # clear entry boxes
    studentid_entry.delete(0, END)
    studentfname_entry.delete(0, END)
    studentlname_entry.delete(0, END)
    studentGPA_entry.delete(0, END)

    stuff.set("Record Updated")



# Buttons
select_button = Button(ws, text="Select Record", command=select_record)
select_button.pack(pady=10)

refresh_button = Button(ws, text="Update Record", command=update_record)
refresh_button.pack(pady=10)

stuff = StringVar()
temp_label = Label(ws, textvariable=stuff, relief=SUNKEN)
temp_label.pack()

ws.mainloop()