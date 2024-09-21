import random
import multiprocessing
import threading
import time
import string

def join_random_numbers():
    numbers = [random.randint(1,100) for _ in range(int(1e7))]
    total_sum = sum(numbers)
    print('Add numbers Task Done')

def join_random_letters():
    letters = [random.choice(string.ascii_letters) for _ in range(int(1e7))]
    joined_letters = "".join(letters)
    print("Joined letters Task Done")

total_start_time = time.time()

serial_start_time = time.time()
join_random_letters()
join_random_numbers()
serial_end_time = time.time()
print(f"The total time taken for serial is : {serial_end_time - serial_start_time} seconds !")

threading_start_time = time.time()
thread1 = threading.Thread(target = join_random_letters)
thread2 = threading.Thread(target = join_random_numbers)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
threading_end_time = time.time()
print(f"The total time taken for threading is : {threading_end_time - threading_start_time} seconds !")


processing_start_time = time.time()
process1 = multiprocessing.Process(target = join_random_letters)
process2 = multiprocessing.Process(target = join_random_numbers)
process1.start()
process2.start()
process1.join()
process2.join()
processing_end_time = time.time()
total_end_time = time.time()

print(f"The total time taken for processing is : {processing_end_time - processing_start_time} seconds !")


thread_speedup = ((serial_end_time - serial_start_time)/(threading_end_time - threading_start_time))
process_speedup = ((serial_end_time - serial_start_time)/(processing_end_time - processing_start_time))

Ts = serial_end_time - serial_start_time
Tpt = threading_end_time - threading_start_time
Tpp = processing_end_time - processing_start_time

total_time = Ts+Tpt+Tpp
total_time2 =total_end_time - total_start_time
np = 4

Pt = Tpt/(Ts+Tpt)
Pp = Tpp/(Ts+Tpp)
P = Pp+Pt

print("Speedup Thread (St): ", thread_speedup)
print("Speedup process (Sp): ", process_speedup)
print("Efficiency of threads: ", thread_speedup/np)
print("Efficiency of process: ", process_speedup/np)
print("The Pt and Pp are: ", Pt, " and ", Pp, " and P is: ",P)

print("Amdahl's speedup: ", 1/((1-P)+(P/np)))
print ("Gustafon's speedup: ", ((1-P)+(4*P)))
