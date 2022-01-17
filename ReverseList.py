# Print list in reverse order using a loop.
list1 = [10, 20, 30, 50]
newlist = reversed(list1)
for item in newlist:
    print(item)
size = len(list1) - 1
for i in range(size, -1):
    print(list1[i])
