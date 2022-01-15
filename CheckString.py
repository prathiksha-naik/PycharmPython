# Count all letters, digits, and special symbols from a given string.
str1 = "P@#yn26at^&i5ve"
count_alphabet = 0
count_digit = 0
count_splcharacter = 0
for string in str1:
    if string.isalpha():
        count_alphabet += 1
    elif string.isdigit():
        count_digit += 1
    else:
        count_splcharacter += 1
print("Alphabet count: ", count_alphabet)
print("Digit count: ", count_digit)
print("SpecialCharacter count: ", count_splcharacter)
