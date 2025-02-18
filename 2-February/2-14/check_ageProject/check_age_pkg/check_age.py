# Returns True if s can be converted to type int.

def is_integer(s):
    try:
        s = int(s)
        return True
    except ValueError:
        return False

# Repeatedly prompts for input until a numeric string is typed.
# Returns the int value that was typed by the user.
def get_int(prompt):
    line = input(prompt)
    while not is_integer(line):
        print("Not an integer; enter an integer or type 0 to stop. ")
        line = input(prompt)
        if line == '0':
            break

    return int(line)

# prompts for a user's age and prints out
# the number of years until the user can retire
def main():
    age = get_int("How old are you? ")
    if age != 0:
        retire = 65 - age
        print("Retire in", retire, "years.")

if __name__ == '__main__':
    main()