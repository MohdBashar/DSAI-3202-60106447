import numpy as np
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

population_size = 100
spread_chance = 0.3
vaccination_rate = np.random.uniform(0.1, 0.5)

population = np.zeros(population_size)

def spread_virus(population):
    
    new_population = population.copy()
    vaccined_ppl_count = vaccination_rate*population_size
    infected_indices = np.random.choice(population_size, int(spread_chance * population_size), replace=False)
    new_population[infected_indices] = 1
    vaccined_indices = np.random.choice(population_size, int(vaccined_ppl_count), replace=False)
    new_population[vaccined_indices] = 0
    return new_population


for _ in range(10):  
      
      population = spread_virus(population)
      if rank != 0:
          comm.send(population, dest=0)
      else:
          for i in range(1, size):
              received_data = comm.recv(source=i)
              population += received_data

final_infected_count = np.sum(population)
infection_rate = final_infected_count / population_size

# Print the infection rate for each process
print(f"Process {rank}: Infection Rate: {infection_rate:.2f}")
