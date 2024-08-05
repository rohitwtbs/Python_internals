# To do three different implementations
# using clas variable
# using decorator
# using singelton metaclass


#  need to go into more detial , how this new behaves difeerently now
class Singelton():
    _count = None
    def __init__(self):
        print("init called")
        pass
    def __new__(cls,*args,**kwargs):
        print("new called")
        if cls._count is None:
            cls = super(Singelton,cls).__new__(cls,*args,**kwargs)
        return cls._count
    
    def tell_id(self):
        return id(self)



obj = Singelton()
obj1 = Singelton()
obj2 = Singelton()

# print(obj.tell_id(),obj1.tell_id(),obj2.tell_id())

print(id(obj),id(obj1), id(obj2))