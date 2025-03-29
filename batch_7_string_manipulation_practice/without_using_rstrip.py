# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# user's input with spaces at the end of the string
user_input = str(input("Input a string with spaces at the end: "))

# ask the user the length of the spaces at the beginning to implement rstrip function
length = int(input("Number of spaces at the beginning (integers): "))
spaces = " " * length

# remove space at the end of the string
input = len(user_input) - 1
while input >= 0 and user_input[input].isspace():
    input -= 1

result = user_input[:input + 1]

# add space to the beginning with specified length
# print output
print(f'\n"{spaces} {result}"')