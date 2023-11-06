# Simulated annealing alghoritm
# We look for the maximum of the function f(x)=...
import math
import random

# Here define the function you're trying to optimize, ex. f(x)=3sin(πx/5)+sin(πx)
def f(x):
    return 3 * math.sin(math.pi * x / 5) + math.sin(math.pi * x)

T = float(input("Enter the starting temperature (e.g., 1.00): "))
print("Temperature is: " + str(T)) 
alpha = float(input("Enter the cooling rate (e.g., 0.9): "))
print("Cooling rate 'alpha' is: " + str(alpha))  

Max = float(input("Enter the range min: "))
print("Min: " + str(Max))  
Min = float(input("Enter the range max: "))
print("Max: " + str(Min))  

x = random.uniform(Max,Min)
print("Starting with x=", x, "f(x)=", f(x))
T_range = [max(Max, x - 2 * T), min(Min, x + 2 * T)] 
print("Range: ", T_range)

# Perform the simulated annealing over x epochs with x trials each
number_of_epochs = int(input("Enter the number of epochs (e.g., 5): "))
print("Temperature is: " + str(number_of_epochs)) 
number_of_trials = int(input("Enter the number of trials (e.g., 3): "))
print("Temperature is: " + str(number_of_trials)) 

for epoch in range(number_of_epochs):
    print("\nEpoch", epoch + 1)
    for trial in range(number_of_trials):
        x_prime = random.uniform(T_range[0], T_range[1])  
        print("  Trial", trial + 1, "x_prime=", x_prime, "f(x_prime)=", f(x_prime))

        # Compare the new solution with the current solution
        if f(x_prime) > f(x):
            print("  New solution {} is better than {}, so accepted".format(x_prime, x))
            x = x_prime
        else:
            acceptance_probability = math.exp((f(x_prime) - f(x)) / T)
            random_zero_one_value = random.uniform(0,1)
            if random_zero_one_value < acceptance_probability:
                x = x_prime
                print(" New solution is worse, but accepted with probability: {}. Random value: {}.".format(acceptance_probability, random_zero_one_value))
            elif random_zero_one_value > acceptance_probability:
                print(" New solution is worse. Probability: {}. Random value: {}.".format(acceptance_probability, random_zero_one_value))
            elif random_zero_one_value == acceptance_probability:
                print("  New solution is worse, rejected")

    # Cool down the temperature for the next epoch
    T *= alpha
    print("  Cooling down to new temperature", T)

# Print the best solution found
print("\nBest solution: x=", x, "f(x)=", f(x))
