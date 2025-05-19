from dataclasses import dataclass

@dataclass
class Circle:
    radius: float
    circumference: float



obj = Circle(5, 31.4)
print(obj)