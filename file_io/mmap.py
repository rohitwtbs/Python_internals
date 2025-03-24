import mmap

def read_with_mmap(file_path):
    try:
        with open(file_path, 'rb') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                # Access the file data like a byte array
                # Example: print(mm[:100])
                # Or iterate through it
                for byte in mm:
                    pass
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"Error reading file: {e}")

file_path = 'your_large_file.txt'
read_with_mmap(file_path)