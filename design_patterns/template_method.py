"""
Template Method Pattern
-----------------------
Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
Template Method lets subclasses redefine certain steps of an algorithm without changing
the algorithm's structure.
"""

from abc import ABC, abstractmethod


# Abstract Class
class DataMiner(ABC):
    """Template method pattern for data mining"""
    
    def mine_data(self):
        """Template method - defines the algorithm structure"""
        self.open_file()
        self.extract_data()
        self.parse_data()
        self.analyze_data()
        self.send_report()
        self.close_file()
    
    @abstractmethod
    def open_file(self):
        pass
    
    @abstractmethod
    def extract_data(self):
        pass
    
    def parse_data(self):
        """Default implementation - can be overridden"""
        print("Parsing data...")
    
    @abstractmethod
    def analyze_data(self):
        pass
    
    def send_report(self):
        """Hook method - optional override"""
        print("Sending report via email...")
    
    def close_file(self):
        """Common implementation for all"""
        print("Closing file and cleaning up\n")


# Concrete Classes
class PDFDataMiner(DataMiner):
    def open_file(self):
        print("Opening PDF file...")
    
    def extract_data(self):
        print("Extracting data from PDF...")
    
    def analyze_data(self):
        print("Analyzing PDF data...")


class CSVDataMiner(DataMiner):
    def open_file(self):
        print("Opening CSV file...")
    
    def extract_data(self):
        print("Extracting data from CSV...")
    
    def parse_data(self):
        print("Parsing CSV with custom parser...")
    
    def analyze_data(self):
        print("Analyzing CSV data...")
    
    def send_report(self):
        print("Sending report via Slack...")


class XMLDataMiner(DataMiner):
    def open_file(self):
        print("Opening XML file...")
    
    def extract_data(self):
        print("Extracting data from XML...")
    
    def analyze_data(self):
        print("Analyzing XML data...")


# Another Example: Beverage Preparation
class Beverage(ABC):
    """Template for preparing beverages"""
    
    def prepare(self):
        """Template method"""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
        print("Beverage is ready!\n")
    
    def boil_water(self):
        print("Boiling water...")
    
    def pour_in_cup(self):
        print("Pouring into cup...")
    
    @abstractmethod
    def brew(self):
        pass
    
    @abstractmethod
    def add_condiments(self):
        pass
    
    def customer_wants_condiments(self):
        """Hook method"""
        return True


class Tea(Beverage):
    def brew(self):
        print("Steeping the tea...")
    
    def add_condiments(self):
        print("Adding lemon...")


class Coffee(Beverage):
    def brew(self):
        print("Dripping coffee through filter...")
    
    def add_condiments(self):
        print("Adding sugar and milk...")


class BlackCoffee(Coffee):
    def customer_wants_condiments(self):
        """Override hook to skip condiments"""
        return False


# Game Example
class Game(ABC):
    """Template for game flow"""
    
    def play(self):
        """Template method"""
        self.initialize()
        self.start_play()
        self.end_play()
    
    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def start_play(self):
        pass
    
    @abstractmethod
    def end_play(self):
        pass


class Chess(Game):
    def initialize(self):
        print("Chess Game Initialized! Setting up board...")
    
    def start_play(self):
        print("Chess Game Started! Make your move...")
    
    def end_play(self):
        print("Chess Game Finished! Checkmate!\n")


class Soccer(Game):
    def initialize(self):
        print("Soccer Game Initialized! Players on field...")
    
    def start_play(self):
        print("Soccer Game Started! Kick off...")
    
    def end_play(self):
        print("Soccer Game Finished! Final whistle!\n")


# Build Process Example
class BuildProcess(ABC):
    """Template for software build process"""
    
    def build(self):
        """Template method"""
        self.clean()
        self.compile()
        self.test()
        self.package()
        if self.should_deploy():
            self.deploy()
        print("Build complete!\n")
    
    def clean(self):
        print("Cleaning build directory...")
    
    @abstractmethod
    def compile(self):
        pass
    
    @abstractmethod
    def test(self):
        pass
    
    @abstractmethod
    def package(self):
        pass
    
    def deploy(self):
        print("Deploying to server...")
    
    def should_deploy(self):
        """Hook method"""
        return False


class AndroidBuild(BuildProcess):
    def compile(self):
        print("Compiling Java/Kotlin code...")
    
    def test(self):
        print("Running Android tests...")
    
    def package(self):
        print("Creating APK...")
    
    def should_deploy(self):
        return True


class iOSBuild(BuildProcess):
    def compile(self):
        print("Compiling Swift code...")
    
    def test(self):
        print("Running iOS tests...")
    
    def package(self):
        print("Creating IPA...")


if __name__ == "__main__":
    # Data Mining Example
    print("=== Data Mining Example ===")
    print("Mining PDF:")
    pdf_miner = PDFDataMiner()
    pdf_miner.mine_data()
    
    print("Mining CSV:")
    csv_miner = CSVDataMiner()
    csv_miner.mine_data()
    
    # Beverage Example
    print("=== Beverage Preparation ===")
    print("Preparing Tea:")
    tea = Tea()
    tea.prepare()
    
    print("Preparing Coffee:")
    coffee = Coffee()
    coffee.prepare()
    
    print("Preparing Black Coffee:")
    black_coffee = BlackCoffee()
    black_coffee.prepare()
    
    # Game Example
    print("=== Game Example ===")
    chess = Chess()
    chess.play()
    
    soccer = Soccer()
    soccer.play()
    
    # Build Process Example
    print("=== Build Process Example ===")
    print("Android Build:")
    android = AndroidBuild()
    android.build()
    
    print("iOS Build:")
    ios = iOSBuild()
    ios.build()
