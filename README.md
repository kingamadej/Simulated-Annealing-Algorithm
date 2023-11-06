# Simulated-Annealing-Algorithm

This repository contains an implementation of the simulated annealing algorithm in Python, designed to find the maximum of a specified function over a given interval. Simulated annealing is a probabilistic technique for approximating the global optimum of a given function. It is a metaheuristic to approximate global optimization in a large search space and is often used when the search space is discrete (e.g., the traveling salesman problem).

## Features

- User-definable function.
- User-definable initial temperature and cooling rate.
- User-definable interval.
- User-definable number of epochs and trials for flexibility in computation effort.

## Getting Started

### Installing

Clone the repository to your local machine:

```
git clone https://github.com/kingamadej/Simulated-Annealing-Algorithm.git
```
Navigate to the cloned directory:
```
cd Simulated-Annealing-Algorithm
```

Run the script using Python:
```
python simulated-annealing-algorithm.py
```
## Usage
To use the algorithm, you will be prompted to enter the following parameters:
- **Starting temperature (T)**: The initial temperature for the algorithm.
- **Cooling rate (alpha)**: The rate at which the temperature cools down each epoch.
- **Range min and max**: The interval within which you want to find the maximum of the function.
- **Number of epochs**: The total number of epochs to run.
- **Number of trials per epoch**: The number of trials to run in each epoch.

### Function (f(x))
You can define the function you want to optimize by changing this fragment of code manually:
```
# Here define the function you're trying to optimize, ex. f(x)=3sin(πx/5)+sin(πx)
def f(x):
    return 3 * math.sin(math.pi * x / 5) + math.sin(math.pi * x)
```




