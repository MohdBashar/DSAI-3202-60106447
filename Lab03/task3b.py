import time
import threading

def calculate_sum_for_threads(start :int = 0, end: int = 10, results_list =[]):
    thread_result = 0
    for i in range(start, end):
        thread_result += i
    results_list.append(thread_result)

n = int(100000)
number_threads = 4
step = n // number_threads #integer division

threads =[]
results = []

for i in range(number_threads):
    start_thread = i * step +1
    end_thread = (i+1)* step
    thread = threading.Thread(target = calculate_sum_for_threads, args=(start_thread, end_thread, results))
    threads.append(thread) #append the completed thread to the threads list
    print(threads)

start_time = time.time()

for i in range(number_threads):
    threads[i].start()

for i in range(number_threads):
    threads[i].join()

end_time = time.time()

parallel_time = start_time-end_time

print("The total time taken for parallel execution is: " + str(end_time - start_time))


start_seq_time = time.time()
calculate_sum_for_threads(end = int(100000))
end_seq_time = time.time()

seq_time = start_seq_time/end_seq_time

print("The total time taken for sequential execution is: " + str(end_seq_time - start_seq_time))


def calculate_speedup(sequential_time, parallel_time):
    """Calculate the speedup of the parallel version."""
    return seq_time / parallel_time

def calculate_efficiency(speedup, num_threads):
    """Calculate the efficiency of the parallel version."""
    return speedup / num_threads

speedup_threading = calculate_speedup(seq_time, parallel_time)
efficiency_threading = calculate_efficiency(speedup_threading, number_threads)

print(f"Speedup (Threading): {speedup_threading:.4f}")
print(f"Efficiency (Threading): {efficiency_threading:.4f}")



def amdahl_speedup(P, num_threads):
    """Calculate speedup using Amdahl's Law.
    P is the fraction of the program that can be parallelized."""
    return 1 / ((1 - P) + (P / num_threads))

# Example: Suppose 90% of the program can be parallelized
P = 0.9  # 90% of the task is parallelizable
speedup_amdahl = amdahl_speedup(P, num_threads)

print(f"Speedup using Amdahl's Law: {speedup_amdahl:.4f}")



# import time
# import threading

# # Function to calculate the sum for a part of the range
# def partial_sum(start, end, result, index):
#     total = 0
#     for i in range(start, end + 1):
#         total += i
#     result[index] = total  # Store the result in a shared list
#     print(result)

# # Sequential sum function for comparison
# def calculate_sum(num):
#     sum = 0
#     for i in range(num + 1):
#         sum += i
#     return sum

# n = int(1e8)
# num_threads = 16  # Number of threads

# # Divide the range into equal parts for each thread
# chunk_size = n // num_threads
# print(chunk_size)
# threads = []
# results = [0] * num_threads  # Shared list to store results from each thread
# print(results)

# # Parallel computation with threading
# start_time = time.time()

# for i in range(num_threads):
#     start = i * chunk_size + 1
#     print(start)
#     # Ensure the last thread covers the remaining range
#     end = (i + 1) * chunk_size if i != num_threads - 1 else n
#     print(end)
#     print(results)
#     thread = threading.Thread(target=partial_sum, args=(start, end, results, i))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# parallel_sum = sum(results)

# end_time = time.time()

# print("The sum of all numbers from 1 to " + str(n) + " = " + str(parallel_sum))
# print("The total time taken for parallel execution is: " + str(end_time - start_time))

# # Serial computation for comparison
# start_time = time.time()
# serial_sum = calculate_sum(n)
# end_time = time.time()
# print("The sum of all numbers from 1 to " + str(n) + " = " + str(serial_sum))
# print("The total time taken for serial execution is: " + str(end_time - start_time))


