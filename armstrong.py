number=int(input("Enter any positive number : "))
def check_armstrong(number):
    if number in range(1,10):
        return True
    order=len(str(number))
    sum=0
    original=number
    while number>0:
        digit=number%10
        sum+=digit**order
        number=number//10
    if sum==original:
        return True
    return False
if check_armstrong(number):
    print('Number is Armstrong')
else:
    print('Number is not Armstrong')


