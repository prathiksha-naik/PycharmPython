string="prathiksha"
half_string=len(string)//2
res=''
for i in range(len(string)):
    if i>=half_string:
        res+=string[i].upper()
    else:
        res=res+string[i]
print("The resultant string: "+str(res))
