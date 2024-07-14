'''Write a Python function that takes two numbers and an operator (as a string) 
and performs the corresponding arithmetic operation 
(addition, subtraction, multiplication, or division).'''

def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        print(num1, ' + ', num2, ' = ', num1+num2)
    elif operator == '-':
        print(num1, ' - ', num2, ' = ', num1-num2)
    elif operator == '*':
        print(num1, ' * ', num2, ' = ', num1*num2)
    elif operator == '/':
        if num2!= 0:
            print(num1, ' / ', num2, ' = ', num1/num2)
        else:
            print("Error: Division by zero is not allowed")
    else:
        print("Wrong operator used...")


one = input("Enter a number: ")
two = input("Enter another number: ")
operator = input("Enter an operator: ")
arithmetic_operation(int(one), int(two), operator)