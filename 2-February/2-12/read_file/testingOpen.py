outfile = open('openMe.txt', 'w')

outfile.write("Hello!\nMy name is Mason. I write many things.")

outfile.close()

infile = open('openMe.txt', 'r')

manyLines = infile.read()
print(manyLines)