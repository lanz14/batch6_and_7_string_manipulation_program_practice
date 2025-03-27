# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# user's input
user_input = str(input("Input a sentence: "))

# using split function to the user input to identify each word
sentence = user_input.split()

# for each word upper case the first letter
upper = []
for word in sentence:
    if word: 
        upper.append(word[0].upper() + word[1:].lower())

output = ' '.join(upper)

# print output
print(f"\n{output}")