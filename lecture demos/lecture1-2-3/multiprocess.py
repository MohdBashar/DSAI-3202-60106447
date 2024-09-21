import multiprocessing
import time

# Here we perform the basic multiprocessing programs as hello world, or demo.
# Function to be executed in a process.

def print_numbers(process_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{process_name}: {count}")


     # Create two processes
process1 = multiprocessing.Process(target=print_numbers,args=("Process-1", 1))
process2 = multiprocessing.Process(target=print_numbers,args=("Process-2", 2))

     # Start the processes
process1.start()
process2.start()

     # Wait for all processes to complete
process1.join()
process2.join()

print("Exiting the Program")