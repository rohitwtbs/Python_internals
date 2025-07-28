# Advanced Memory Management & GC Questions

## 1. Reference Counting Deep Dive
Explain how Python's reference counting works at the C level. What happens when you do `a = b` vs `a = b[:]` for a list? Why doesn't reference counting alone solve all memory management issues?

## 2. Cyclic Reference Detection Algorithm
Describe Python's cycle detection algorithm. How does it identify unreachable cycles? What's the difference between the three generations in Python's generational garbage collector?

## 3. Memory Pools and Object Allocation
Explain Python's memory allocation strategy. What are PyMalloc, object pools, and memory arenas? Why does Python maintain separate pools for small objects?

## 4. Weak References and Callbacks
What are weak references and when would you use them? How do `weakref.ref()` and `weakref.proxy()` differ? Write code showing how weak reference callbacks work.

## 5. Memory Optimization Techniques
Compare memory usage of `list` vs `tuple` vs `array.array` vs `collections.deque`. When would you use `__slots__`? What are the trade-offs?

## 6. GC Thresholds and Tuning
Explain `gc.set_threshold()` parameters. How do you profile memory leaks? What tools would you use to debug memory issues in production?

## 7. Interning and Singleton Objects
Which objects does Python intern automatically? How does string interning work? What's the difference between `sys.intern()` and automatic interning?

## 8. Context Managers and Resource Management
How do context managers help with memory management? Write a custom context manager that tracks object creation/destruction.
