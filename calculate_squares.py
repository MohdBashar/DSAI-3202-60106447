from mpi4py import MPI
import numpy as np
import time

def square_numbers(start, end):
    return [i**2 for i in range(start, end+1)]

def main(n):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()  # Get the process ID (rank)
    size = comm.Get_size()  # Get the number of processes

    if rank == 0:
        # Root process
        chunks = np.array_split(range(1, n+1), size)
    else:
        chunks = None

    # Scatter the chunks of data to all processes
    chunk = comm.scatter(chunks, root=0)

    # Each process computes the squares for its chunk
    start_time = time.time()
    result = square_numbers(chunk[0], chunk[-1])

    # Gather the results at the root process
    all_results = comm.gather(result, root=0)

    # Root process combines all the results
    if rank == 0:
        squares = [item for sublist in all_results for item in sublist]
        print(f"Final array size: {len(squares)}")
        print(f"Last square: {squares[-1]}")
        print(f"Time taken: {time.time() - start_time} seconds")

if __name__ == "__main__":
    n = int(1e8)  # You can set a smaller value for testing
    main(n)
