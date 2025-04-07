import threading

def hello(): print("Hello")

t = threading.Thread(target=hello)
t.start()
t.join()

# Try to restart
t.start()
#  threads can't be restarted