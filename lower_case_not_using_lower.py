# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# user's input
character_inputs = str(input("Input a text: "))

# set a variable to an empty string
lower_case = ""

# check from A to Z if there is a capital letter
# convert capital into lower case
for letter in character_inputs:
    if "A" <= letter <= "Z":
        lower_case += chr(ord(letter) + 32)
    else:
        lower_case += letter

# print output
print(lower_case)