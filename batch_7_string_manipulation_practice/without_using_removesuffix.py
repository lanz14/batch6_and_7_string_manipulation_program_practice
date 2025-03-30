# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# user's input
user_input = str(input("Input a string: "))

# ask the user what character at the end of the string to be removed
remove = str(input("String to be removed at the end?: "))

# print output
formatted = user_input.replace(f"{remove}", "")
print(formatted)