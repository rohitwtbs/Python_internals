from multiprocessing import Process, Value

def increment(shared_x):
    for _ in range(100000):
        shared_x.value += 1

if __name__ == "__main__":
    x = Value('i', 0) 
    p1 = Process(target=increment, args=(x,))
    p2 = Process(target=increment, args=(x,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(x.value)