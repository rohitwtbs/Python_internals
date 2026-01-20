"""
Observer Pattern
----------------
Defines a one-to-many dependency between objects so that when one object changes state,
all its dependents are notified and updated automatically.
"""

from abc import ABC, abstractmethod


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


# Subject (Observable)
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


# Concrete Observers
class ConcreteObserverA(Observer):
    def update(self, subject):
        print(f"ObserverA: Reacted to state change -> {subject.state}")


class ConcreteObserverB(Observer):
    def update(self, subject):
        if subject.state >= 5:
            print(f"ObserverB: Reacted to state change -> {subject.state}")


# Real-world Example: Stock Price Monitoring
class Stock(Subject):
    def __init__(self, symbol, price):
        super().__init__()
        self.symbol = symbol
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
        print(f"\n{self.symbol} price changed to ${value}")
        self.notify()


class Investor(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, stock):
        print(f"{self.name} notified: {stock.symbol} is now ${stock.price}")


class TradingBot(Observer):
    def __init__(self, buy_threshold, sell_threshold):
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
    
    def update(self, stock):
        if stock.price < self.buy_threshold:
            print(f"TradingBot: BUY signal for {stock.symbol} at ${stock.price}")
        elif stock.price > self.sell_threshold:
            print(f"TradingBot: SELL signal for {stock.symbol} at ${stock.price}")


if __name__ == "__main__":
    # Basic example
    print("=== Basic Observer Pattern ===")
    subject = Subject()
    
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    
    subject.attach(observer_a)
    subject.attach(observer_b)
    
    subject.state = 3
    subject.state = 7
    
    # Real-world example
    print("\n=== Stock Monitoring Example ===")
    apple_stock = Stock("AAPL", 150.0)
    
    investor1 = Investor("John")
    investor2 = Investor("Sarah")
    bot = TradingBot(buy_threshold=140, sell_threshold=160)
    
    apple_stock.attach(investor1)
    apple_stock.attach(investor2)
    apple_stock.attach(bot)
    
    apple_stock.price = 145.0
    apple_stock.price = 135.0
    apple_stock.price = 165.0
    
    # Detach an observer
    apple_stock.detach(investor2)
    print("\n--- After detaching Sarah ---")
    apple_stock.price = 170.0
