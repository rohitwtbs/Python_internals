
import time
from functools import wraps

# Simple decorator to measure execution time
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Decorator with parameters
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

# Decorator for logging
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

# Example functions without using @ syntax
def calculate_square(n):
    return n * n

def greet(name):
    return f"Hello, {name}!"

def slow_function():
    time.sleep(1)
    return "Done"

# Manually decorating functions (without @ syntax)
timed_square = timer_decorator(calculate_square)
logged_greet = log_function(greet)
repeated_slow = repeat(3)(slow_function)

if __name__ == "__main__":
    # Using decorated functions
    print("\nTesting timer decorator:")
    result = timed_square(5)
    print(f"Result: {result}")
    
    print("\nTesting logging decorator:")
    result = logged_greet("Alice")
    print(f"Final result: {result}")
    
    print("\nTesting repeat decorator:")
    results = repeated_slow()
    print(f"Results from multiple calls: {results}")
    
    # Demonstrating multiple decorators
    multi_decorated = timer_decorator(log_function(calculate_square))
    print("\nTesting multiple decorators:")
    result = multi_decorated(4)
    print(f"Final result: {result}")
    
    # Equivalent to using @ syntax:
    # @timer_decorator
    # @log_function
    # def calculate_square(n):
    #     return n * n
