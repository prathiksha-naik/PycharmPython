#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
num=int(input("Enter the number: "))
previous=0
sum=0
for current in range(num):
    if current==0:
        previous=0
        sum=current+previous
        print("Current number is {} , previous number is {} and sum of current number and previous number: {}".format(current,previous,sum))
    else:
        previous=current-1
        sum=current+previous
        print("Current number is {} , previous number is {} and sum of current number and previous number: {}".format(current,previous,sum))

