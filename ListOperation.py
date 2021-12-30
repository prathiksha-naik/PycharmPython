def addThisNumber(number):
    if number>=1 and number<=2:
        return 2
    elif number>=3 and number<10:
        return 5
    elif number>=10 and number<=12:
        return 11
    else:
        return number
def mydef(a):
    for x in a:
        if x>(addThisNumber(x)):
            print("will be printed",x)
        else:
            answer=addThisNumber(x+12)
            print(answer+addThisNumber(10))
myList=[4,8,15,4,1,34,2]
mydef(myList)