
class Car():
    def __init_(self):
        pass
    @staticmethod
    def start():
        print("Car started")
    # @classmethod
    # def stop(cls):
    #     print("Car stopped")

    @classmethod
    def stop():
        print("Car stopped")

bmw = Car()
bmw.start()
bmw.stop()
Car.start()
Car.stop()


#  todo
#  try to implement these decorator from scratch