import mmap
import time

def read_with_mmap(file_path):
    try:
        with open(file_path, 'rb') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                # Process the file in chunks for better performance
                chunk_size = 1024 * 1024  # 1 MB chunks
                for offset in range(0, len(mm), chunk_size):
                    chunk = mm[offset:offset + chunk_size]
                    print(chunk)
                    # Process the chunk (e.g., print the first few bytes)
                    # Example: print(chunk[:10])
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"Error reading file: {e}")

file_path = r"C:\Users\rohit\Videos\Captures\eee.mp4"
start_time = time.time()
read_with_mmap(file_path)
print("time taken ", time.time() - start_time)