# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# user's input
user_input = str(input("Input a string: "))

# upper the first character and then lower the rest of the string
while len(user_input):
    convert = user_input[0].upper() + user_input[1:].lower()
    break

# print output
print(f"\n{convert}")