import itertools
import time
import random

def calculate_total_distance(route, distances):
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[num_cities - 1]][route[0]]  # Return to the start
    return total_distance

def brute_force_tsp(distances):
    print("Distance Matrix:")
    for row in distances:
        print(row)
    num_cities = len(distances)
    cities = list(range(num_cities))
    shortest_route = None
    shortest_distance = float('inf')
    iterations = 0
    start_time = time.time()

    for permutation in itertools.permutations(cities):
        total_distance = calculate_total_distance(permutation, distances)
        iterations += 1
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_route = permutation

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nShortest Route Bruteforce: {shortest_route}")
    print(f"Shortest Distance Bruteforce: {shortest_distance}")
    print(f"Total Iterations Bruteforce: {iterations}")
    return shortest_route, shortest_distance, elapsed_time, iterations

#shortest_route, shortest_distance, elapsed_time, iterations = brute_force_tsp(distances)
