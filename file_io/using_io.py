import io
import time

def read_buffered(filename):
    with open(filename, 'rb') as f:
        buffered_reader = io.BufferedReader(f)
        while True:
            chunk = buffered_reader.read(8192) #8kb chunks
            print(chunk)
            if not chunk:
                break

file_path = r"C:\Users\rohit\Videos\Captures\eee.mp4"
start_time = time.time()
read_buffered(file_path)
print("time taken by the read ", time.time() - start_time)