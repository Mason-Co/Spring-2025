# Programmer: Mason Colacicco
# Date: March
# Program: Course Information

def main():
    # initialize that dictionaries
    rooms = {"CS101":3004, "CS102":4501, "CS103":6755, "NT110":1244, "CM241":1411}
    instructors = {"CS101":"Haynes", "CS102":"Alvarado", "CS103":"Rich", "NT110":"Burke", "CM241":"Lee"}
    meetings = {"CS101":"8:00 a.m.", "CS102":"9:00 a.m.", "CS103":"10:00 a.m.", "NT110":"11:00 a.m.", "CM241":"1:00 p.m."}

    # user input
    course = input("Enter the course code: ")

    # Check for value error and display data
    try:
        print("Room:", rooms[course])
        print("Instructor:", instructors[course])
        print("Meeting Time:", meetings[course])
    except KeyError:
        print("Invalid course code")

# Call main function
if __name__ == "__main__":
    main()