# from mpi4py import MPI
# import numpy as np

# # Initialize MPI
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()

# # Define parameters
# population_size = 100  # Population per process
# spread_chance = 0.3  # Chance of virus spreading
# vaccination_rate = np.random.uniform(0.1, 0.5)  # Random vaccination rate for each process

# # Initialize population array (0 = uninfected, 1 = infected)
# population = np.zeros(population_size, dtype=int)

# # Infect a small initial group in rank 0 process
# if rank == 0:
#     infected_indices = np.random.choice(population_size, int(0.1 * population_size), replace=False)
#     population[infected_indices] = 1

# def spread_virus(population, spread_chance, vaccination_rate):
#     new_population = population.copy()
#     for i in range(len(population)):
#         if population[i] == 0:  # If uninfected
#             # Check neighbors for infection and apply vaccination rate
#             if np.random.rand() < spread_chance * (1 - vaccination_rate):
#                 new_population[i] = 1
#     return new_population


# # Time steps for the simulation
# time_steps = 10

# for _ in range(time_steps):
#     # Each process updates its population based on virus spread
#     population = spread_virus(population, spread_chance, vaccination_rate)
    
#     # Send updated population to the root process
#     if rank != 0:
#         comm.send(population, dest=0)
#     else:
#         # Gather data from other processes
#         for i in range(1, size):
#             received_data = comm.recv(source=i)
#             population += received_data  # Aggregate infected individuals

# # Calculate the total infected and infection rate for each process
# total_infected = np.sum(population)
# infection_rate = total_infected / population_size

# # Output the infection rate for each process
# print(f"Process {rank} Infection Rate: {infection_rate}")


from mpi4py import MPI
import numpy as np

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define parameters
population_size = 100  # Population per process
spread_chance = 0.3  # Chance of virus spreading
vaccination_rate = np.random.uniform(0.1, 0.5)  # Random vaccination rate for each process

# Initialize population array (0 = uninfected, 1 = infected)
population = np.zeros(population_size, dtype=int)

# Infect a small initial group in each process
infected_indices = np.random.choice(population_size, int(0.1 * population_size), replace=False)
population[infected_indices] = 1

def spread_virus(population, spread_chance, vaccination_rate):
    new_population = population.copy()
    for i in range(len(population)):
        if population[i] == 0:  # If uninfected
            # Check neighbors for infection and apply vaccination rate
            if np.random.rand() < spread_chance * (1 - vaccination_rate):
                new_population[i] = 1
    return new_population

# Time steps for the simulation
time_steps = 10

for _ in range(time_steps):
    # Each process updates its population based on virus spread
    population = spread_virus(population, spread_chance, vaccination_rate)

# Calculate the total infected and infection rate for each process
total_infected = np.sum(population)
infection_rate = total_infected / population_size

# Output the infection rate for each process
print(f"Process {rank} Infection Rate: {infection_rate}, Vaccination Rate: {vaccination_rate:.2f}, Total Infected: {total_infected}")
