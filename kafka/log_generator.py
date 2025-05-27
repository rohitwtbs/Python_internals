import time
from datetime import datetime
from multiprocessing import Process, cpu_count

def write_log(process_id):
    i = 1
    while True:  # Infinite loop for continuous logging
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("app.log", "a") as log_file:
            log_file.write(f"[{timestamp}] Process {process_id}: Log entry {i}\n")
        print(f"[{timestamp}] Process {process_id}: Log entry {i}")
        i += 1
        time.sleep(1)

if __name__ == "__main__":
    # Create (or overwrite) the log file
    with open("app.log", "w") as log_file:
        log_file.write("Log file created.\n")

    num_cores = cpu_count()
    processes = []

    for pid in range(num_cores):
        p = Process(target=write_log, args=(pid,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()