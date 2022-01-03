#Using recurion adding sum of n natural numbers
def sum_num(n):
    if n<=1:
        return n
    return n+sum_num(n-1)

p=sum_num(10)
print(p)
