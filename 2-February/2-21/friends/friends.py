# Programmer: Mason Colacicco
# Date: February
# Program: Friends

def main():
    # Initialize list and index
    friends = ['Brock', 'Ben', 'Klein', 'Mason', 'Karsten']
    index = 0

    # Loop to display data
    while index < len(friends):
        print(friends[index])
        index +=1

    # Change names
    friends[2] = 'Billy'
    friends[4] = 'Jerry'

    # Separate lists
    print()

    # Reset index
    index = 0
    # Loop to display data
    while index < len(friends):
        print(friends[index])
        index +=1

# Call main function
if __name__ == '__main__':
    main()