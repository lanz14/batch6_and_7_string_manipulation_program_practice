# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# user's input
user_input = input("Input a string: ")

# ask the user a single character to count within a string
char_count = input("Character to count (e.g. letter 'a'): ")

# if the user did not enter a single character, it will alert the user to input only single character to count
if len(char_count) != 1:
    print("\nPlease enter only single character from a-z.")

# if the user input a single character, it will print the amount of times it appeared
else:
    counter = 0
    for char in user_input:
        if char == char_count:
            counter += 1
    print(f"\n'{char_count}' appears {counter} times.")