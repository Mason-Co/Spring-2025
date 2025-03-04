# Programmer: Mason Colacicco
# Date: February
# Program: Count Char Type

def main():
    # Initialize all numbers and contents
    nbr_upper = nbr_lower = nbr_space = nbr_digit = 0
    contents = ''

    # Open and read file then close
    infile = open('text.txt', 'r')
    contents = infile.read()
    infile.close()

    # Loop each char
    for char in contents:
        if char.islower():
            nbr_lower += 1
        elif char.isupper():
            nbr_upper += 1
        elif char.isdigit():
            nbr_digit += 1
        elif char.isspace():
            nbr_space += 1

    print("Uppercase:", nbr_upper)
    print("Lowercase:", nbr_lower)
    print("Digit:", nbr_digit)
    print("Space:", nbr_space)


if __name__ == "__main__":
    main()