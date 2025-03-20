import time
def read_large_file(file_path, chunk_size = 200):
    try:
        with open(file_path,'rb')  as file:
            while True:
                chunk = file.read(chunk_size)
                if (not chunk):
                    break
                print(chunk)
    except FileNotFoundError:
        print("error")
    except IOError as e:
        print(e)


file_path = r"C:\Users\rohit\Videos\Captures\eee.mp4"
start_time = time.time()
read_large_file(file_path)
print("time taken ", time.time() - start_time)