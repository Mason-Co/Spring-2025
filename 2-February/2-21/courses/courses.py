# Programmer: Mason Colacicco
# Date: February
# Program: Courses

def main():
    # Define courses
    courses = ['COS2005','LDR1011','MAT3051','COS1015','CYS2034','MAT2018','COS4011','COS3007','COS2042','MIS3014']

    # ask for course
    course = input("What course ID would you like to check for? ")

    # check for course
    if course not in courses:
        print("That course doesn't exist.")
    else:
        print("That course is offered.")

# Call main function
if __name__ == "__main__":
    main()