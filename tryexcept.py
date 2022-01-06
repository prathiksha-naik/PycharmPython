def div(number):
    try:
        print(42/number)
    except ZeroDivisionError:
        print("zero division error")
div(2)
div(0)
div(12)
