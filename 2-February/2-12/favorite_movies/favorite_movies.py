# Programmer: Mason Colacicco
# Date: February
# Program: Favorite Movies


def main():
    # Initialize variable
    newMovies = []

    # User input
    for i in range(0,4):
        newMovies.append(input(f"What is your #{i+1} favorite movie? "))

    # Open file to write
    outfile = open('movies.txt', 'a')
    for movie in newMovies:
        outfile.write(movie + '\n')

    # Close file
    outfile.close()

    # Open file to read
    infile = open('movies.txt', 'r')
    # Read contents
    file_contents = infile.read()
    # Close file
    infile.close()

    # Display data
    print(file_contents)

# Call main function
if __name__ == '__main__':
    main()