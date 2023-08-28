import random
import math
import time

def calculate_total_distance(route, distances):
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[num_cities - 1]][route[0]]  # Return to the start
    return total_distance

def simulated_annealing_tsp(distances, initial_temperature=10000, cooling_rate=0.995, num_iterations=10000):
    print("Distance Matrix:")
    for row in distances:
        print(row)
    num_cities = len(distances)
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, distances)

    best_route = current_route.copy()
    best_distance = current_distance

    temperature = initial_temperature

    start_time = time.time()
    count = 0
    for iteration in range(num_iterations):
        new_route = current_route.copy()
        count +=1
        # Perform a random swap of two cities in the route
        i, j = random.sample(range(num_cities), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]

        new_distance = calculate_total_distance(new_route, distances)
        delta_distance = new_distance - current_distance

        if delta_distance < 0 or random.random() < math.exp(-delta_distance / temperature):
            current_route = new_route
            current_distance = new_distance

            if current_distance < best_distance:
                best_route = current_route.copy()
                best_distance = current_distance

        temperature *= cooling_rate

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nBest Route SA: {best_route}")
    print(f"Best Distance SA: {best_distance}")
    print(f"Total Iterations SA: {count}")
    return best_route, best_distance, elapsed_time

#best_route, best_distance, elapsed_time = simulated_annealing_tsp(distances, initial_temperature, cooling_rate, num_iterations)
