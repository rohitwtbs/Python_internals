import sys
import gc


a = [1,2,3,4]

b = a
# print(sys.__dict__)
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))
del a