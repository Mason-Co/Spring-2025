# Programmer: Mason Colacicco
# Date: March
# Program: Friend Book

def main():
    # Create dictionary
    book = {"Ben":"Blaine","Klein":"St. Paul","Brock":"Brooklyn Park","Aziel":"Wayzata","Josie":"Apple Valley"}

    # display data
    print(book)

    # Add entries
    book["Breanna"] = "Minneapolis"
    book["Mason"] = "Lakeville"

    # display data
    print(book)

    # Check and delete entries
    if "Breanna" in book:
        del book["Breanna"]
    if "Mason" in book:
        del book["Mason"]

    # Display data in a table
    print("Name\tCity")
    for i in book:
        if len(i) < 4:
            print(f"{i}\t\t{book[i]}")
        else:
            print(f"{i}\t{book[i]}")

# Call main function
if __name__ == "__main__":
    main()