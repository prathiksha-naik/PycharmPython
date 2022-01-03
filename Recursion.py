#Recursion
def fact_recursion(n):
    if n==0 or n==1:
        return 1
    return n*fact_recursion(n-1)
s=fact_recursion(5)
print(s)
