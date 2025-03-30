# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# user's input
user_input = str(input("Input a text: "))

# check if the inputted string is all in lower case
lower_case = True

for letter in user_input:
    if "A" <= letter <= "Z":
        lower_case = False
        break

# print "True" if the input is all in lower case
if lower_case:
    print("True")

# print "False" if not all input is in lower case
else:
    print("False")