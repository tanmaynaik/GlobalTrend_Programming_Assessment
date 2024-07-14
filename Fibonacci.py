'''Write a Python function to compute the nth 
Fibonacci number using recursion.'''

def fibonacci(n):
    
    if n < 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


p = int(input("Enter a number: "))
print(f"The {p}th Fibonacci number is {fibonacci(p)}")
