import threading
import time

def print_number(thread_name: str ,delay, start_time):
    start_time = 0
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        since_start = time.time() - start_time
        print(f"Since start: {since_start}, {thread_name}:{count}")

start_time = time.time()

thread1 = threading.Thread(target = print_number, args=("Thread-1",1,start_time))
thread2 = threading.Thread(target = print_number, args=("Thread-2",2, start_time))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting the program")