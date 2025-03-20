# Programmer: Mason Colacicco
# Date: March
# Program: Friend Book 2 Electric Boogaloo

def main():
    # Create dictionary
    book = {"Ben": "Blaine", "Klein": "St. Paul", "Brock": "Brooklyn Park", "Aziel": "Wayzata", "Josie": "Apple Valley"}

    # display data
    print(book)

    # Add entries
    book["Breanna"] = "Minneapolis"
    book["Mason"] = "Lakeville"

    # Display data in a table
    print("Name\t\tCity")
    for i in book:
        if len(i) < 4:
            print(f"{i}\t\t\t{book[i]}")
        elif len(i) > 7:
            print(f"{i}\t{book[i]}")
        else:
            print(f"{i}\t\t{book[i]}")


# Call main function
if __name__ == "__main__":
    main()