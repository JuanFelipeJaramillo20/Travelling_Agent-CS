
# Travelling Agent

The Traveling Salesman Problem (TSP) is a classic challenge in the field of combinatorial optimization and computer theory. In simple terms, the problem involves finding the shortest route that passes through a set of cities, visiting each city exactly once and returning to the starting city.

The TSP has applications in various fields such as logistics, route planning, circuit design, network optimization, and more. However, as the number of cities increases, finding the optimal solution becomes increasingly complex and computationally demanding. This is due to the factorial increase in the number of possible routes with the number of cities, leading to scalability issues.

Numerous algorithms and approaches have been developed to address the TSP, including exact methods like exhaustive search and dynamic programming, as well as approximate approaches like the nearest neighbor algorithm, the insertion algorithm, and simulated annealing. Additionally, the TSP has been used to illustrate concepts in computational complexity theory, such as NP-complete problems and heuristic algorithms.

This project was created for the Computer Simulation course at Universidad del Valle, the idea is to use 2 solutions, one is bruteforce and the other one is the famous Simulated annealing algorithm. Once the simulations are completed, we will compare the difference between the two solutions in the biggest aspects.

You can check the results of this simulation in the following report:





## Run Locally

Clone the project:

```bash
  git clone https://github.com/JuanFelipeJaramillo20/Travelling_Agent-CS.git
```

Go to the project directory:

```bash
  cd Travelling_Agent-CS
```

Change the configurations to apply to your current needs:

```python
NUM_CITIES = 100
NUM_ITERATIONS = 100000
```

Run the ```main.py``` file.


## Screenshots

![5 cities](https://i.imgur.com/UlQWql9.png)

![10 cities](https://i.imgur.com/UlQWql9.png)
