import time
import importlib
import random

# Import the two scripts
brute_force_script = importlib.import_module("Brute_Force")
simulated_annealing_script = importlib.import_module("Simulated_annealing")

NUM_CITIES = 100
NUM_ITERATIONS = 100000

# Generate random distance matrix
distances = []
for _ in range(NUM_CITIES):
    row = [random.randint(1, 100) for _ in range(NUM_CITIES)]
    distances.append(row)

# Measure execution time for brute-force method
start_time_brute_force = time.time()
brute_force_script.brute_force_tsp(distances)
end_time_brute_force = time.time()
elapsed_time_brute_force = end_time_brute_force - start_time_brute_force

# Measure execution time for simulated annealing method
start_time_simulated_annealing = time.time()
simulated_annealing_script.simulated_annealing_tsp(distances, NUM_ITERATIONS=100000)
end_time_simulated_annealing = time.time()
elapsed_time_simulated_annealing = end_time_simulated_annealing - start_time_simulated_annealing

print(f"Brute-Force Execution Time: {elapsed_time_brute_force:.6f} seconds")
print(f"Simulated Annealing Execution Time: {elapsed_time_simulated_annealing:.6f} seconds")


