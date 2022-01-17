# Count the total number of digits in a number.
# For example, the number is 75869, so the output should be 5.
number = int(input("Enter the number: "))
count = 0
while number != 0:
    number = number // 10
    count = count + 1
print("Total digits are: ", count)
