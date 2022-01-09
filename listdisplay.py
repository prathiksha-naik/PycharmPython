# Display numbers divisible by 5 from a list.
number = int(input("Enter the number of values required to be entered in list: "))
num = []
for i in range(number):
    num.append(int(input("Enter the values into list: ")))
print(num)
divisible = []
notdivisible = []
for list in num:
    if list % 5 == 0:
        divisible.append(list)
    else:
        notdivisible.append(list)
print("List value {} is not divisible by 5".format(notdivisible))
print("List value {} is divisible by 5".format(divisible))
