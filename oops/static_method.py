class StacticClass():
    def __init__(self):
        pass
    @staticmethod
    def tell_id(any):
        return id(any)
    



# calling static method without creating object
print(StacticClass.tell_id(StacticClass))
print(StacticClass.tell_id())