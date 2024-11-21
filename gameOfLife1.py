import numpy as np
from mpi4py import MPI

def update_local_grid(local_grid, top_ghost_row, bottom_ghost_row):
    rows, cols = local_grid.shape
    updated_grid = np.copy(local_grid)

    # Pad the grid with ghost rows for easier computation
    padded_grid = np.vstack([top_ghost_row, local_grid, bottom_ghost_row])

    # Apply the Game of Life rules
    for i in range(1, rows + 1):  # Loop over local rows
        for j in range(cols):  # Loop over columns
            # Count alive neighbors
            neighbors_sum = (
                padded_grid[i-1, (j-1) % cols] + padded_grid[i-1, j] + padded_grid[i-1, (j+1) % cols] +
                padded_grid[i, (j-1) % cols] + padded_grid[i, (j+1) % cols] +
                padded_grid[i+1, (j-1) % cols] + padded_grid[i+1, j] + padded_grid[i+1, (j+1) % cols]
            )

            # Apply rules
            if local_grid[i-1, j] == 1:  # Alive cell
                if neighbors_sum < 2 or neighbors_sum > 3:
                    updated_grid[i-1, j] = 0  # Dies
            elif neighbors_sum == 3:  # Dead cell with 3 neighbors
                updated_grid[i-1, j] = 1  # Becomes alive

    return updated_grid

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the grid dimensions
grid_rows, grid_cols = 100, 100
rows_per_process = grid_rows // size

# Initialize the local grid with random values
local_grid = np.random.choice([0, 1], size=(rows_per_process, grid_cols))

# Simulation parameters
num_steps = 10  # Number of simulation steps

# Ghost rows for boundary exchange
top_ghost_row = np.zeros(grid_cols, dtype=int)
bottom_ghost_row = np.zeros(grid_cols, dtype=int)

# Simulation loop
for step in range(num_steps):
    # Communication of ghost rows with neighbors
    top_neighbor = rank - 1 if rank > 0 else MPI.PROC_NULL  # Top neighbor process
    bottom_neighbor = rank + 1 if rank < size - 1 else MPI.PROC_NULL  # Bottom neighbor process

    # Exchange rows with neighbors
    comm.Sendrecv(sendbuf=local_grid[0, :], dest=top_neighbor, recvbuf=bottom_ghost_row, source=bottom_neighbor)
    comm.Sendrecv(sendbuf=local_grid[-1, :], dest=bottom_neighbor, recvbuf=top_ghost_row, source=top_neighbor)

    # Update the local grid
    local_grid = update_local_grid(local_grid, top_ghost_row, bottom_ghost_row)

    # Gather all local grids on root process
    full_grid = None
    if rank == 0:
        full_grid = np.zeros((grid_rows, grid_cols), dtype=int)  # Root process holds the full grid
    comm.Gather(local_grid, full_grid, root=0)

    # Visualization on root process
    if rank == 0:
        print(f"Step {step + 1}: Full Grid")
        for row in full_grid:
            print("".join("■" if cell else "□" for cell in row))  # Print alive cells as ■ and dead cells as □ 
        print("\n" + "=" * 100)  # Separator between steps
        print()