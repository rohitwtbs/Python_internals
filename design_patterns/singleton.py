"""
Singleton Pattern
-----------------
Ensures a class has only one instance and provides a global point of access to it.
"""


# Method 1: Using __new__
class SingletonNew:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.value = None


# Method 2: Using Metaclass
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Database Connection"
    
    def query(self, sql):
        return f"Executing: {sql}"


# Method 3: Using Decorator
def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton
class Logger:
    def __init__(self):
        self.logs = []
    
    def log(self, message):
        self.logs.append(message)
        print(f"LOG: {message}")


if __name__ == "__main__":
    # Test SingletonNew
    s1 = SingletonNew()
    s1.value = 42
    s2 = SingletonNew()
    print(f"s1 is s2: {s1 is s2}")  # True
    print(f"s2.value: {s2.value}")  # 42
    
    # Test Database (Metaclass)
    db1 = Database()
    db2 = Database()
    print(f"\ndb1 is db2: {db1 is db2}")  # True
    print(db1.query("SELECT * FROM users"))
    
    # Test Logger (Decorator)
    logger1 = Logger()
    logger1.log("First message")
    logger2 = Logger()
    logger2.log("Second message")
    print(f"\nlogger1 is logger2: {logger1 is logger2}")  # True
    print(f"Total logs: {len(logger1.logs)}")  # 2
