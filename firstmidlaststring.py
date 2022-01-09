# Write a program to create a new string made of an input string’s first, middle, and last character.
str1 = 'James'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
print("Length of string: ", l)
print("First character of string:",res)
# Get middle index number
mi = int(l / 2)
middle = str1[mi]
print("Middle character of string: ", middle)
# Get middle character and add it to result
res = res + middle

last = str1[l - 1]
print("Last character of string: ", last)

# Get last character and add it to result
res = res + last

print("New String:", res)
