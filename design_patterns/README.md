# Design Patterns in Python

This directory contains implementations of common design patterns in Python with practical examples.

## Design Patterns Included

### Creational Patterns
1. **Singleton Pattern** (`singleton.py`)
   - Ensures a class has only one instance
   - Examples: Database connections, Logger, Configuration manager
   - Three implementations: `__new__`, Metaclass, and Decorator

2. **Factory Pattern** (`factory.py`)
   - Creates objects without specifying exact classes
   - Examples: Vehicle factory, GUI components (Abstract Factory)
   - Includes both Simple Factory and Abstract Factory patterns

### Structural Patterns
3. **Adapter Pattern** (`adapter.py`)
   - Converts interface of a class into another interface
   - Examples: Media player, Payment gateways, Database adapters
   - Makes incompatible interfaces work together

4. **Decorator Pattern** (`decorator.py`)
   - Adds new functionality to objects dynamically
   - Examples: Coffee shop orders, Function decorators, Class decorators
   - Both structural (object) and Python function decorators

### Behavioral Patterns
5. **Observer Pattern** (`observer.py`)
   - Defines one-to-many dependency between objects
   - Examples: Stock price monitoring, Event systems
   - Automatic notification when subject changes state

6. **Strategy Pattern** (`strategy.py`)
   - Encapsulates family of algorithms
   - Examples: Payment methods, Sorting algorithms, Compression strategies
   - Algorithms are interchangeable at runtime

7. **Command Pattern** (`command.py`)
   - Encapsulates requests as objects
   - Examples: Smart home remote, Text editor with undo
   - Supports undo/redo operations and macro commands

8. **Template Method Pattern** (`template_method.py`)
   - Defines skeleton of algorithm, subclasses override steps
   - Examples: Data mining, Beverage preparation, Game flow, Build process
   - Hook methods allow optional customization

## Running Examples

Each file can be run independently:

```bash
python singleton.py
python factory.py
python observer.py
python decorator.py
python strategy.py
python adapter.py
python command.py
python template_method.py
```

## Pattern Categories

### When to Use Each Pattern

- **Singleton**: When you need exactly one instance (e.g., database connection pool)
- **Factory**: When object creation is complex or you want to decouple creation logic
- **Observer**: When changes in one object should notify multiple dependents
- **Decorator**: When you want to add responsibilities to objects dynamically
- **Strategy**: When you have multiple algorithms for a task and want to switch at runtime
- **Adapter**: When you need to use existing classes with incompatible interfaces
- **Command**: When you want to parameterize objects with operations or support undo
- **Template Method**: When you have a fixed algorithm structure with variable steps

## Key Concepts

### SOLID Principles Applied
- **Single Responsibility**: Each class has one reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes must be substitutable for their base types
- **Interface Segregation**: Many specific interfaces are better than one general
- **Dependency Inversion**: Depend on abstractions, not concretions

### Common Pattern Elements
- **Abstract Base Classes (ABC)**: Define interfaces in Python
- **Composition over Inheritance**: Patterns often favor composition
- **Encapsulation**: Hide implementation details
- **Polymorphism**: Different implementations of the same interface

## Additional Resources

- Gang of Four (GoF) Design Patterns book
- Python-specific pattern implementations
- Real-world use cases in frameworks like Django, Flask
