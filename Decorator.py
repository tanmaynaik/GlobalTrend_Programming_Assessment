'''Write a Python decorator that measures the execution time 
of a function and logs it. Apply this decorator to a 
function that performs a computationally expensive task.'''

import time
import logging

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function {func.__name__} executed in {execution_time:.2f} seconds")
        return result
    return wrapper

# Example usage:

@timer_decorator
def computationally_expensive_task(n):
    result = 0
    for i in range(n):
        result += i ** 2
    print(result)

logging.basicConfig(level=logging.INFO)

computationally_expensive_task(1000000)