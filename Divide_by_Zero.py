'''Write a Python function that divides two numbers and handles the case
 where the divisor is zero by returning a custom error message.'''
def divide(a,b):
    try:
        print(a,"/",b,"=",a/b)
    except ZeroDivisionError:
        print("Divisor cannot be zero")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
divide(a,b)