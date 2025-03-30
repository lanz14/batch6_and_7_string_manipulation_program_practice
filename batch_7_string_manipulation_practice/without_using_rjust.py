# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# user input
user_input = str(input("Input a string: "))

# ask the user the length of space character added at the beginning
space_length = int(input("Number of space length (integers):"))
spaces = " " * space_length

# implement the length and print the output