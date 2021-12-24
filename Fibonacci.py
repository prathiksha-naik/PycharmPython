number=int(input("Enter the number"))
first_number=0
second_number=1
count=0
if number<=0:
    print("Enter the positive integer")
elif number==1:
    print(first_number)
else:
    print("Fibonacci sequence: ")
    while count<number:
        print(first_number)
        third_number=first_number+second_number
        #UPDATE VALUES
        first_number=second_number
        second_number=third_number
        count+=1
