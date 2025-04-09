import os
import multiprocessing
from multiprocessing import Queue, current_process

def safe_list_dir(path):
    """Safely list directory contents, handling permission errors."""
    try:
        with os.scandir(path) as it:
            return [entry.path for entry in it]
    except PermissionError:
        return []
    except Exception as e:
        print(f"[{current_process().name}] Error accessing {path}: {e}")
        return []

def worker(dir_queue, file_queue):
    """Worker process that scans directories."""
    while True:
        path = dir_queue.get()
        if path is None:
            break  # End signal

        sub_paths = safe_list_dir(path)
        for sub_path in sub_paths:
            if os.path.isdir(sub_path):
                dir_queue.put(sub_path)
            else:
                file_queue.put(sub_path)

def main(start_path="/"):
    manager = multiprocessing.Manager()
    dir_queue = manager.Queue()
    file_queue = manager.Queue()

    dir_queue.put(start_path)

    num_workers = multiprocessing.cpu_count()
    workers = []

    for _ in range(num_workers):
        p = multiprocessing.Process(target=worker, args=(dir_queue, file_queue))
        p.start()
        workers.append(p)

    try:
        while any(p.is_alive() for p in workers) or not file_queue.empty():
            while not file_queue.empty():
                file_path = file_queue.get()
                print(f"File: {file_path}")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    finally:
        # Tell workers to shut down
        for _ in workers:
            dir_queue.put(None)
        for p in workers:
            p.join()

if __name__ == "__main__":
    main("/")
