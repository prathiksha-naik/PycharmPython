"Print characters from a string that are present at an even index number"
string=input("Enter the string as input: ")
length=len(string)
for i in range(length):
    if i%2==0:
        print("character from a string that is present at an even index number is: ",end="")
        print(string[i])
        

