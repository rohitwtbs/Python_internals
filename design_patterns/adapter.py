"""
Adapter Pattern
---------------
Converts the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
"""

from abc import ABC, abstractmethod


# Target Interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, file_type, filename):
        pass


# Adaptee (incompatible interface)
class VLCPlayer:
    def play_vlc(self, filename):
        return f"Playing VLC file: {filename}"


class MP4Player:
    def play_mp4(self, filename):
        return f"Playing MP4 file: {filename}"


# Adapter
class MediaAdapter(MediaPlayer):
    def __init__(self, file_type):
        if file_type == "vlc":
            self.player = VLCPlayer()
        elif file_type == "mp4":
            self.player = MP4Player()
        else:
            self.player = None
    
    def play(self, file_type, filename):
        if file_type == "vlc":
            return self.player.play_vlc(filename)
        elif file_type == "mp4":
            return self.player.play_mp4(filename)
        return "Unsupported format"


# Client
class AudioPlayer(MediaPlayer):
    def play(self, file_type, filename):
        if file_type == "mp3":
            return f"Playing MP3 file: {filename}"
        elif file_type in ["vlc", "mp4"]:
            adapter = MediaAdapter(file_type)
            return adapter.play(file_type, filename)
        else:
            return f"Invalid media type: {file_type}"


# Real-world Example: Payment Gateway Adapter
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Third-party payment systems (Adaptees)
class StripePayment:
    def make_stripe_payment(self, amount, currency="USD"):
        return f"Stripe: Charged {currency} {amount}"


class PayPalPayment:
    def send_paypal_payment(self, amount, email):
        return f"PayPal: Sent ${amount} to {email}"


class SquarePayment:
    def square_charge(self, amount_cents):
        return f"Square: Charged {amount_cents} cents"


# Adapters
class StripeAdapter(PaymentProcessor):
    def __init__(self):
        self.stripe = StripePayment()
    
    def process_payment(self, amount):
        return self.stripe.make_stripe_payment(amount)


class PayPalAdapter(PaymentProcessor):
    def __init__(self, email):
        self.paypal = PayPalPayment()
        self.email = email
    
    def process_payment(self, amount):
        return self.paypal.send_paypal_payment(amount, self.email)


class SquareAdapter(PaymentProcessor):
    def __init__(self):
        self.square = SquarePayment()
    
    def process_payment(self, amount):
        amount_cents = int(amount * 100)
        return self.square.square_charge(amount_cents)


# Database Adapter Example
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql):
        pass


class PostgreSQL:
    def pg_connect(self, host, port):
        return f"PostgreSQL connected to {host}:{port}"
    
    def execute_query(self, query):
        return f"PostgreSQL executing: {query}"


class MongoDB:
    def mongo_connect(self, connection_string):
        return f"MongoDB connected: {connection_string}"
    
    def find(self, collection, filter_dict):
        return f"MongoDB find in {collection}: {filter_dict}"


class PostgreSQLAdapter(Database):
    def __init__(self, host="localhost", port=5432):
        self.pg = PostgreSQL()
        self.host = host
        self.port = port
    
    def connect(self):
        return self.pg.pg_connect(self.host, self.port)
    
    def query(self, sql):
        return self.pg.execute_query(sql)


class MongoDBAdapter(Database):
    def __init__(self, connection_string="mongodb://localhost:27017"):
        self.mongo = MongoDB()
        self.connection_string = connection_string
    
    def connect(self):
        return self.mongo.mongo_connect(self.connection_string)
    
    def query(self, sql):
        # Convert SQL-like query to MongoDB format
        return self.mongo.find("collection", {"field": "value"})


if __name__ == "__main__":
    # Media Player Example
    print("=== Media Player Adapter ===")
    player = AudioPlayer()
    print(player.play("mp3", "song.mp3"))
    print(player.play("vlc", "movie.vlc"))
    print(player.play("mp4", "video.mp4"))
    print(player.play("avi", "video.avi"))
    
    # Payment Gateway Adapter
    print("\n=== Payment Gateway Adapter ===")
    stripe = StripeAdapter()
    print(stripe.process_payment(100.50))
    
    paypal = PayPalAdapter("user@example.com")
    print(paypal.process_payment(75.00))
    
    square = SquareAdapter()
    print(square.process_payment(50.25))
    
    # Database Adapter
    print("\n=== Database Adapter ===")
    pg_db = PostgreSQLAdapter()
    print(pg_db.connect())
    print(pg_db.query("SELECT * FROM users"))
    
    mongo_db = MongoDBAdapter()
    print(mongo_db.connect())
    print(mongo_db.query("find users"))
