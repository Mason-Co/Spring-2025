# Programmer: Mason Colacicco
# Date: January
# Program: Average Sales

# Initialize Variables
total=count=avg=0

# Loop for the sales
while True:
    num = float(input("What was the sales amount? "))
    if num == 0:
        break
    else:
        total += num
        count += 1

# Error trap for 0 sales
if count == 0:
    print("There were 0 sales.")
else: # Calculate the average
    avg = total/count

# Display data
print(f"There were {count} sales with a total of ${total:,.2f}. The average sale was ${avg:,.2f}.")