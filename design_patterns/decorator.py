"""
Decorator Pattern
-----------------
Attaches additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending functionality.
"""

from abc import ABC, abstractmethod


# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def description(self):
        pass


# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5.0
    
    def description(self):
        return "Simple Coffee"


# Decorator Base Class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
    def description(self):
        return self._coffee.description()


# Concrete Decorators
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1.5
    
    def description(self):
        return self._coffee.description() + ", Milk"


class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5
    
    def description(self):
        return self._coffee.description() + ", Sugar"


class WhippedCream(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2.0
    
    def description(self):
        return self._coffee.description() + ", Whipped Cream"


# Function Decorator Example
def timer_decorator(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    
    return wrapper


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    
    return wrapper


@timer_decorator
@logging_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Class-based Decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Object Decorator Pattern
    print("=== Coffee Shop Example ===")
    
    # Simple coffee
    coffee = SimpleCoffee()
    print(f"{coffee.description()} costs ${coffee.cost()}")
    
    # Coffee with milk
    coffee = Milk(SimpleCoffee())
    print(f"{coffee.description()} costs ${coffee.cost()}")
    
    # Coffee with milk and sugar
    coffee = Sugar(Milk(SimpleCoffee()))
    print(f"{coffee.description()} costs ${coffee.cost()}")
    
    # Fully loaded coffee
    coffee = WhippedCream(Sugar(Milk(SimpleCoffee())))
    print(f"{coffee.description()} costs ${coffee.cost()}")
    
    # Function Decorators
    print("\n=== Function Decorators ===")
    # fibonacci(5)  # Uncomment to test (will be slow due to recursion)
    
    print("\n=== Class-based Decorator ===")
    print(greet("Alice"))
    print(greet("Bob"))
    print(greet("Charlie"))
    print(f"Total calls: {greet.count}")
