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

references = gc.collect()


print(references)  # Why this prints 0 




# Reference cycle example
class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

# Create a cycle
node1 = Node(1)
node2 = Node(2)
node1.ref = node2
node2.ref = node1  # Cycle created!

# Even after deleting variables, objects might stay in memory
# due to the cycle, until garbage collector runs
del node1, node2

# Force garbage collection
collected = gc.collect()
print(f"Collected {collected} objects")