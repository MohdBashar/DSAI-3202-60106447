import time
import threading

def calculate_sum_for_threads(start: int = 0, end: int = 10, results_list=[]):
    """
    Function to calculate the sum of numbers within a given range (start to end) 
    and store the result in the results_list.

    Args:
        start (int): Starting number for the range (inclusive).
        end (int): Ending number for the range (inclusive).
        results_list (list): List to store the result from each thread.
    """
    thread_result = 0
    for i in range(start, end + 1):
        thread_result += i
    results_list.append(thread_result)  # Append the result to the shared list

# Main Program
if __name__ == "__main__":
    n = int(1e8)  # Large number to sum up to
    number_threads = 4  # Number of threads
    step = n // number_threads  # Divide the range into equal chunks

    threads = []  # List to store thread objects
    results = []  # List to store the sum results from each thread

    # Create and start threads
    for i in range(number_threads):
        start_time = time.time()  # Record the start time for parallel execution

        start_thread = i * step + 1
        end_thread = (i + 1) * step
        thread = threading.Thread(target=calculate_sum_for_threads, args=(start_thread, end_thread, results))
        threads.append(thread)  # Append each thread to the threads list
        print(threads)

    # Start each thread
    for i in range(number_threads):
        threads[i].start()

    # Wait for all threads to finish
    for i in range(number_threads):
        threads[i].join()

    end_time = time.time()  # Record the end time for parallel execution

    print("The total time taken for parallel execution is: " + str(end_time - start_time))

    # Sequential execution for comparison
    start_seq_time = time.time()
    calculate_sum_for_threads(end=int(1e8))  # Perform summation sequentially
    end_seq_time = time.time()

    print("The total time taken for sequential execution is: " + str(end_seq_time - start_seq_time))

    # Calculate performance metrics
    parallel_time = end_time - start_time
    seq_time = end_seq_time - start_seq_time

    # Calculate the sum from all threads
    thread_sum = sum(results)
    print("The total sum of the threading is: ", thread_sum)

    # Calculate speedup and efficiency
    speedup_threading = seq_time / parallel_time
    efficiency_threading = speedup_threading / number_threads

    print(f"Speedup (Threading): {speedup_threading:.4f}")
    print(f"Efficiency (Threading): {efficiency_threading:.4f}")

    # Amdahl's Law and Gustafson's Law calculations
    total_time = seq_time + parallel_time
    P = parallel_time / total_time

    # Amdahl's Law
    print(f"Speedup using Amdahl's Law: ", 1 / ((1 - P) + (P / number_threads)))

    # Gustafson's Law
    print("Speedup using Gustafson's Law: ", (1 - P) + (number_threads * P))


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


