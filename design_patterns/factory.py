"""
Factory Pattern
---------------
Provides an interface for creating objects without specifying their exact classes.
"""

from abc import ABC, abstractmethod


# Product Interface
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


# Concrete Products
class Car(Vehicle):
    def drive(self):
        return "Car is driving on the road"
    
    def stop(self):
        return "Car stopped"


class Bike(Vehicle):
    def drive(self):
        return "Bike is riding on the road"
    
    def stop(self):
        return "Bike stopped"


class Truck(Vehicle):
    def drive(self):
        return "Truck is hauling cargo"
    
    def stop(self):
        return "Truck stopped"


# Factory
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")


# Abstract Factory Pattern
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


# Concrete Products for Windows
class WindowsButton(Button):
    def render(self):
        return "Rendering Windows button"


class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering Windows checkbox"


# Concrete Products for Mac
class MacButton(Button):
    def render(self):
        return "Rendering Mac button"


class MacCheckbox(Checkbox):
    def render(self):
        return "Rendering Mac checkbox"


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()


if __name__ == "__main__":
    # Simple Factory Pattern
    print("=== Simple Factory Pattern ===")
    factory = VehicleFactory()
    
    car = factory.create_vehicle("car")
    print(car.drive())
    print(car.stop())
    
    bike = factory.create_vehicle("bike")
    print(bike.drive())
    
    # Abstract Factory Pattern
    print("\n=== Abstract Factory Pattern ===")
    os_type = "windows"  # or "mac"
    
    if os_type == "windows":
        gui_factory = WindowsFactory()
    else:
        gui_factory = MacFactory()
    
    button = gui_factory.create_button()
    checkbox = gui_factory.create_checkbox()
    
    print(button.render())
    print(checkbox.render())
