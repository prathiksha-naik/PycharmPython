#string is palindrome or not
def palin(string):
    if string==string[::-1]:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")
def palindrome(string):
    text="".join(reversed(string))
    if string == text:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")
def palin_drome(string):
    w=''
    for i in string:
        w=i+w
    if w==string:
        print("It is palindrome")
    else:
        print("It is not palindrome")
    

palin("malayalam")
palin_drome("malayalam")
palindrome("malayalam")

    
