# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to control the number of rows
while row < size:
    # For loop to print asterisks in each row
    for i in range(size):
        print("*", end="")
    
    # Move to the next line after printing one full row
    print()
    
    # Increase row counter
    row += 1
