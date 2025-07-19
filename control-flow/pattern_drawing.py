# pattern_drawing.py
# This scrippt draws a square pattern 

# Step 1: Prompt the user for input
size = int(input("Enter the size of the pattern: "))

# step 2: Initialize row counter for the while loop
row=0

# Step 3: Outer while loop for rows
while row < size:
    # Step 4: Inner for loop for columns
    for column in range (size):
        print("*", end="")

    # Step 5: Move to the next line after each row is printed
    print()

    # Step 6: Increment the row counter
    row += 1