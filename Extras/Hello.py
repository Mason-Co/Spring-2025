more = input("First Letter of First Name: ")
fname = []
while len(more) == 1:
    fname.append(more)
    more = input("Next letter (2 letters to esc): ")


for letter in fname:
    print(letter, end="")