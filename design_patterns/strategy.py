"""
Strategy Pattern
----------------
Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.
"""

from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        return f"Paid ${amount} using PayPal account: {self.email}"


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin wallet: {self.wallet_address[:10]}..."


# Context
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
    
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy
    
    def checkout(self):
        total = sum(item["price"] for item in self.items)
        if self.payment_strategy is None:
            return "No payment method selected"
        return self.payment_strategy.pay(total)


# Another Example: Sorting Strategies
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSort(SortStrategy):
    def sort(self, data):
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class PythonSort(SortStrategy):
    def sort(self, data):
        return sorted(data)


class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data)


# Compression Strategy Example
class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, data):
        pass


class ZipCompression(CompressionStrategy):
    def compress(self, data):
        return f"ZIP compressed: {data} -> {len(data) * 0.6:.0f} bytes"


class RarCompression(CompressionStrategy):
    def compress(self, data):
        return f"RAR compressed: {data} -> {len(data) * 0.5:.0f} bytes"


class TarGzCompression(CompressionStrategy):
    def compress(self, data):
        return f"TAR.GZ compressed: {data} -> {len(data) * 0.7:.0f} bytes"


class FileCompressor:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def compress_file(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
        return self.strategy.compress(data)


if __name__ == "__main__":
    # Payment Strategy Example
    print("=== Payment Strategy ===")
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000)
    cart.add_item("Mouse", 50)
    cart.add_item("Keyboard", 100)
    
    # Pay with credit card
    cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456", "123"))
    print(cart.checkout())
    
    # Pay with PayPal
    cart.set_payment_strategy(PayPalPayment("user@example.com"))
    print(cart.checkout())
    
    # Pay with Bitcoin
    cart.set_payment_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    print(cart.checkout())
    
    # Sorting Strategy Example
    print("\n=== Sorting Strategy ===")
    data = [64, 34, 25, 12, 22, 11, 90]
    
    sorter = Sorter(BubbleSort())
    print(f"Bubble Sort: {sorter.sort_data(data)}")
    
    sorter.set_strategy(QuickSort())
    print(f"Quick Sort: {sorter.sort_data(data)}")
    
    sorter.set_strategy(PythonSort())
    print(f"Python Sort: {sorter.sort_data(data)}")
    
    # Compression Strategy Example
    print("\n=== Compression Strategy ===")
    data = "This is a sample text file content" * 100
    
    compressor = FileCompressor(ZipCompression())
    print(compressor.strategy.compress(data))
    
    compressor.strategy = RarCompression()
    print(compressor.strategy.compress(data))
    
    compressor.strategy = TarGzCompression()
    print(compressor.strategy.compress(data))
