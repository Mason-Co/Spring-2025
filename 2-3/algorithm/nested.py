# Programmer: Mason Colacicco
# Date: February
# Program: Algorithm

# Table Header
print(f"Length\tWidth\tVolume")

# Loop for values
for length in range(1,11):
    for width in range(1,6):
        print(f"{length}\t\t{width}\t\t{length*width*.25}")