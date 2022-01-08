# Reverse a Number using a while loop.
digit = int(input("Enter the number: "))
reversed_number = 0
while digit != 0:
    container = digit % 10
    reversed_number = reversed_number * 10 + container
    digit //= 10
print("The reversed number is:", reversed_number)
