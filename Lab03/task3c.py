import multiprocessing
import multiprocessing.process
import time

# Make a program which calculates sum for each indivitual process, when we call it in the processing. 
# Then make sure that each result of each indivitual process is appended to the list !

def calculate_sum_for_process(start : int = 0, stop: int = 10, result_list = [] ):
    process_result = 0
    for i in range(start, stop):
        process_result += i
    result_list.append(process_result)

n = int(1e8)
num_processes = 4
processes = []
result = []
chunk_size = n // num_processes  #ie the number divided to each process indivitually chunks.

for i in range(num_processes):
    start_process = i * chunk_size + 1 # starts from 1
    end_process = (i+1) * chunk_size # ends at the last chunk number 
    process = multiprocessing.Process(target = calculate_sum_for_process, args = (start_process, end_process, result))
    processes.append(process) #append the completed process to the list
    print(processes)


start_time = time.time()

for i in range(num_processes):
    processes[i].start()  #starting each of the process that is stored in the processes list

for i in range(num_processes):
    processes[i].join()  #waiting until the process has finished.

end_time = time.time()

print("The total time taken for parallel execution is: " + str(end_time - start_time))


start_seq_time = time.time()
calculate_sum_for_process(stop = int(1e8))
end_seq_time = time.time()
print("The total time taken for sequential execution is: " + str(end_seq_time - start_seq_time))

seq_time = end_seq_time - start_seq_time
parallel_time = end_time-start_time


def calculate_speedup(sequential_time, parallel_time):
    """Calculate the speedup of the parallel version."""
    return sequential_time / parallel_time

def calculate_efficiency(speedup, number_processes):
    """Calculate the efficiency of the parallel version."""
    return speedup / number_processes

speedup_threading = calculate_speedup(seq_time, parallel_time)
efficiency_threading = calculate_efficiency(speedup_threading, num_processes)

print(f"Speedup (Threading): {speedup_threading:.4f}")
print(f"Efficiency (Threading): {efficiency_threading:.4f}")

total_time = seq_time + parallel_time
P = parallel_time/total_time

print(f"Speedup using Amdahl's Law:" , 1/((1-P)+(P/num_processes)))
print ("Sppedup using Gustafson's speedup: ", ((1-P)+(4*P)))