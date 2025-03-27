# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# user's input
user_input = str(input("Enter a string: "))

# ask the user how many spaces to add at the end
length = int(input("Enter the total length: "))

# add space to the end with specified number
spaces = " " * length

formatted = user_input + spaces

# print output
print(f'\nResult: "{formatted}"')