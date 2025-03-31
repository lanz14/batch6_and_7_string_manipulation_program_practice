# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# user's input
user_input = input("Input a sentence: ")

# ask the user what substring to find
sub_str = input("Input a substring to find: ")

# find the substring starting from the end
result = -1

for i in range(len(user_input) - len(sub_str), -1, -1):
    if user_input[i:i+len(sub_str)] == sub_str:
        result = i
        break

# print output
if result == -1:
    print(f"'{sub_str}' is not found")
else:
    print(result)