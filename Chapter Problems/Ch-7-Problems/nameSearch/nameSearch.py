# Programmer: Mason Colacicco
# Date: February
# Program: Name Search

def main():
    # Open boy names file, read, and close
    infile = open("boysnames.txt", 'r')
    boys = infile.read().split('\n')
    infile.close()

    # Open girl names file, read, and close
    infile = open("girlsnames.txt", 'r')
    girls = infile.read().split('\n')
    infile.close()

    # User input for names
    boy = input("Enter a boy name (q to pass): ").capitalize()
    girl = input("Enter a girl name (q to pass): ").capitalize()

    # Options to find common names (or pass)
    if boy == 'Q':
        pass
    else:
        if boy not in boys:
            print(f"{boy} is not a common boy name.")
        else:
            print(f"{boy} is a common boy name.")
    if girl == 'Q':
        pass
    else:
        if girl not in girls:
            print(f"{girl} is not a common girl name.")
        else:
            print(f"{girl} is a common girl name.")


# Call main function
if __name__ == '__main__':
    main()