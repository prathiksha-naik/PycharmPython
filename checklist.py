# Take input for list from user check if the first and last number of a list is the same .
num = []
number = int(input("Enter the number required to be added into list: "))
for i in range(number):
    num.append(input("Enter value to the list: "))


def first_last_same(num):
    print("list:", num)
    first_num = num[0]
    last_num = num[-1]
    if first_num == last_num:
        return True
    else:
        return False


a = first_last_same(num)
print(a)
