# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# user's input
user_input = str(input("Enter a string: "))

# identify small letters, then convert to uppercase
result = ""

for lower in user_input:
    if 'a' <= lower <= 'z':
        uppercase_char = chr(ord(lower) - 32)
        result += uppercase_char

    else:
        result += lower

# print output