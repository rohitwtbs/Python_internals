import sys
import gc


a = [1,2,3,4]

b = a
# print(sys.__dict__)
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))
del a

# lets see for a cyclic referrence
# gc.collect()  # Uncomment to force garbage collection


class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

    def add_adress(self, node):
        self.next = node


node1 = Node(1)
node2 = Node(2)
node1.add_adress(node2)
node2.add_adress(node1)

print(gc.collect())  # This will collect the cyclic references