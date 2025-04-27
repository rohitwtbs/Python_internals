# import time
# def read_large_file(file_path, chunk_size = 200):
#     try:
#         with open(file_path,'rb')  as file:
#             while True:
#                 chunk = file.read(chunk_size)
#                 if (not chunk):
#                     break
#                 print(chunk)
#     except FileNotFoundError:
#         print("error")
#     except IOError as e:
#         print(e)


# file_path = r"C:\Users\rohit\Videos\Captures\eee.mp4"
# start_time = time.time()
# read_large_file(file_path)
# print("time taken ", time.time() - start_time)




import time
import threading

def process_chunk(chunk):
    # Simulate processing the chunk (replace with your actual logic)
    # time.sleep(0.01)  # Add a small delay to simulate work
    print(chunk)  # Or your actual chunk processing

def read_large_file_threaded(file_path, chunk_size=2000):
    try:
        with open(file_path, 'rb') as file:
            threads = []
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                thread = threading.Thread(target=process_chunk, args=(chunk,))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join() #wait for all threads to complete.

    except FileNotFoundError:
        print("error")
    except IOError as e:
        print(e)


file_path = r"C:\Users\rohit\Videos\Captures\eee.mp4"
start_time = time.time()
read_large_file_threaded(file_path)
print("time taken ", time.time() - start_time)



import time
import multiprocessing

def process_chunk_mp(chunk):
    """Simulates processing a chunk (replace with your actual logic)."""
    # Replace the print statement with your actual chunk processing.
    print(chunk)  # Or your actual chunk processing

def read_large_file_multiprocessing(file_path, chunk_size=200):
    """Reads a large file in chunks using multiprocessing."""
    try:
        with open(file_path, 'rb') as file:
            processes = []
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                process = multiprocessing.Process(target=process_chunk_mp, args=(chunk,))
                processes.append(process)
                process.start()

            for process in processes:
                process.join()  # Wait for all processes to complete.

    except FileNotFoundError:
        print("error: File not found")
    except IOError as e:
        print(f"error: {e}")

if __name__ == "__main__":  # Important for multiprocessing on Windows
    file_path = r"C:\Users\rohit\Videos\Captures\eee.mp4"
    start_time = time.time()
    read_large_file_multiprocessing(file_path)
    print("time taken ", time.time() - start_time)