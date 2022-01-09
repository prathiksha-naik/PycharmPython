number = int(input("Enter the number to display its multiplication table: "))
for i in range(0, 10+1):
    multi = number * i
    print("{} x {} = {}".format(number, i, multi))
print("MULTIPLICATION TABLE OF {}".format(number))
