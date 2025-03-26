# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# user's input
# using replace(), to remove the spaces
user_input = input("Input characters with spaces at the beginning: ").replace(" ", "")

# print output
print(user_input)