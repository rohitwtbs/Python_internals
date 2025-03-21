import io

def read_buffered(filename):
    with open(filename, 'rb') as f:
        buffered_reader = io.BufferedReader(f)
        while True:
            chunk = buffered_reader.read(8192) #8kb chunks
            if not chunk:
                break


read_buffered()