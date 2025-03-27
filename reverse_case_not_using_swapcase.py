# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# user's input
user_input = str(input("Input a string: "))

# reverse case the letters
reverse_case = ""

for letter in user_input:
    if 'a' <= letter <= 'z':

        reverse_case += chr(ord(letter) - 32)

    elif 'A' <= letter <= 'Z':
        reverse_case += chr(ord(letter) + 32)

    else:
        reverse_case += letter

# print the reverse cased letters
print(f"\n{reverse_case}")