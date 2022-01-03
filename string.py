#Python program to print even length words in a string
string="I am Prathiksha"
s=string.split()
for word in s:
    if len(word)%2==0:
        print("Even length is: "+word)

