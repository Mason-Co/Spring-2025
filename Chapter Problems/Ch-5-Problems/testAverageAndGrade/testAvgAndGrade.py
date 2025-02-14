# Programmer: Mason Colacicco
# Date: February
# Program: Test Average and Grade

def main():
    tests = []

    # Loop 5 times
    for i in range(0,5):
        tests.append(int(input(f"Test Score {i+1}: ")))

    # Call functions
    letter_grades = determine_grade(tests)
    test_avg = calc_average(tests)
    show_table(tests,letter_grades,test_avg)


def calc_average(arr):
    # Initialize variable
    avg = 0

    # Loop for each test
    for val in arr:
        avg += val
    avg = avg/len(arr)
    return avg

def determine_grade(arr):
    # Initialize variable
    grades = []

    # Loop for each test
    for test in arr:
        if test >= 90:
            grades.append("A")
        elif test >= 80:
            grades.append("B")
        elif test >= 70:
            grades.append("C")
        elif test >= 60:
            grades.append("D")
        else:
            grades.append("F")
    return grades

def show_table(score,grade,average):
    # Display data
    print(f"Test\tScore\tGrade")
    for i in range(0,len(score)):
        print(f"{i+1}\t\t{score[i]}\t\t{grade[i]}")
    print(f"Average Score: {average:.1f}")


# Call main function
main()