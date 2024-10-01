import multiprocessing
import time

# Function to calculate the sum for a range of numbers and store it in a shared list
def calculate_sum_for_process(start: int, stop: int, result_list, index):
    process_result = sum(range(start, stop + 1))
    result_list[index] = process_result  # Store result in the shared list at the correct index

# Main program
if __name__ == "__main__":
    n = int(1e8)  # Large number
    num_processes = 4  # Number of processes
    chunk_size = n // num_processes  # Divide the range into equal chunks

    # Create a manager to handle shared memory
    with multiprocessing.Manager() as manager:
        result = manager.list([0] * num_processes)  # Shared list to store the results of each process
        processes = []

        # Create and start processes
        for i in range(num_processes):
            start_process = i * chunk_size + 1
            end_process = (i + 1) * chunk_size if i != num_processes - 1 else n
            process = multiprocessing.Process(target=calculate_sum_for_process, args=(start_process, end_process, result, i))
            processes.append(process)

        # Record start time for parallel execution
        start_time = time.time()

        # Start each process
        for process in processes:
            process.start()

        # Wait for all processes to finish
        for process in processes:
            process.join()

        # Record end time for parallel execution
        end_time = time.time()

        # Calculate the total sum from all processes
        total_sum = sum(result)
        print(f"Parallel Sum: {total_sum}")
        print("The total time taken for parallel execution is: " + str(end_time - start_time))

        # Sequential execution for comparison
        start_seq_time = time.time()
        sequential_sum = sum(range(1, n + 1))
        end_seq_time = time.time()
        print(f"Sequential Sum: {sequential_sum}")
        print("The total time taken for sequential execution is: " + str(end_seq_time - start_seq_time))

        # Performance metrics
        seq_time = end_seq_time - start_seq_time
        parallel_time = end_time - start_time

        def calculate_speedup(sequential_time, parallel_time):
            """Calculate the speedup of the parallel version."""
            return sequential_time / parallel_time

        def calculate_efficiency(speedup, number_processes):
            """Calculate the efficiency of the parallel version."""
            return speedup / number_processes

        # Compute speedup and efficiency
        speedup_parallel = calculate_speedup(seq_time, parallel_time)
        efficiency_parallel = calculate_efficiency(speedup_parallel, num_processes)

        print(f"Speedup (Multiprocessing): {speedup_parallel:.4f}")
        print(f"Efficiency (Multiprocessing): {efficiency_parallel:.4f}")

        # Amdahl's Law and Gustafson's Law calculations
        P = parallel_time / (seq_time + parallel_time)

        # Amdahl's Law
        speedup_amdahl = 1 / ((1 - P) + (P / num_processes))
        print(f"Speedup using Amdahl's Law: {speedup_amdahl:.4f}")

        # Gustafson's Law
        speedup_gustafson = (1 - P) + (num_processes * P)
        print(f"Speedup using Gustafson's Law: {speedup_gustafson:.4f}")



# import multiprocessing
# import multiprocessing.process
# import time

# # Make a program which calculates sum for each indivitual process, when we call it in the processing. 
# # Then make sure that each result of each indivitual process is appended to the list !

# def calculate_sum_for_process(start : int = 0, stop: int = 10, result_list = [] ):
#     process_result = 0
#     for i in range(start, stop+1):
#         process_result += i
#     result_list.append(process_result)

# n = int(1e8)
# num_processes = 4
# processes = []
# result = []
# chunk_size = n // num_processes  #ie the number divided to each process indivitually chunks.

# for i in range(num_processes):
#     start_process = i * chunk_size + 1 # starts from 1
#     end_process = (i+1) * chunk_size # ends at the last chunk number 
#     process = multiprocessing.Process(target = calculate_sum_for_process, args = (start_process, end_process, result))
#     processes.append(process) #append the completed process to the list
#     print(processes)


# start_time = time.time()

# for i in range(num_processes):
#     processes[i].start()  #starting each of the process that is stored in the processes list

# for i in range(num_processes):
#     processes[i].join()  #waiting until the process has finished.

# end_time = time.time()

# print("The total time taken for parallel execution is: " + str(end_time - start_time))


# start_seq_time = time.time()
# calculate_sum_for_process(stop = int(1e8))
# end_seq_time = time.time()
# print("The total time taken for sequential execution is: " + str(end_seq_time - start_seq_time))

# seq_time = end_seq_time - start_seq_time
# parallel_time = end_time-start_time


# def calculate_speedup(sequential_time, parallel_time):
#     """Calculate the speedup of the parallel version."""
#     return sequential_time / parallel_time

# def calculate_efficiency(speedup, number_processes):
#     """Calculate the efficiency of the parallel version."""
#     return speedup / number_processes

# speedup_threading = calculate_speedup(seq_time, parallel_time)
# efficiency_threading = calculate_efficiency(speedup_threading, num_processes)

# print(f"Speedup (Threading): {speedup_threading:.4f}")
# print(f"Efficiency (Threading): {efficiency_threading:.4f}")

# total_time = seq_time + parallel_time
# P = parallel_time/total_time

# print(f"Speedup using Amdahl's Law:" , 1/((1-P)+(P/num_processes)))
# print ("Sppedup using Gustafson's speedup: ", ((1-P)+(4*P)))