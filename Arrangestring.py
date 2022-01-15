"""Given string contains a combination of the lower and upper case letters. 
Write a program to arrange the characters of a string so that all lowercase letters should come first."""
string = "PSNprathi"
lower = []
upper = []
for strings in string:
    if strings.islower():
        lower.append(strings)
    else:
        upper.append(strings)
joinstring = ''.join(lower + upper)
print(str(joinstring))

