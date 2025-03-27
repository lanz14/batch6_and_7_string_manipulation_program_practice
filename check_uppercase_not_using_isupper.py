# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# user's input
input = str(input("Input a text: "))

# check if the inputs are in all upper case
upper_case = True

for letter in input:
    if "a" <= letter <= "z":
        upper_case = False
        break 

# print "True" if the inputs are all in upper case
if upper_case:
    print("True")

# print "False" if the inputs are not all in upper case
else:
    print("False")