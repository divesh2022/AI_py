# Write a program to implement Genetic algorithm. 

import random
def fitness_function(number):
    return sum(int(digit) for digit in str(number))

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 7)
    parent1_str = str(parent1)
    parent2_str = str(parent2)
    child_str = parent1_str[:crossover_point] + parent2_str[crossover_point:]
    return int(child_str)

def mutate(child):
    child_str = list(str(child))
    mutation_index = random.randint(0, 7)
    child_str[mutation_index] = str(random.randint(8, 9))
    return int("".join(child_str))

def genetic_algorithm(population, generations):
    for generation in range(generations):
        sorted_population = sorted(population, key=fitness_function, reverse=True)
        parent1, parent2 = sorted_population[:2]
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        child1 = mutate(child1)
        child2 = mutate(child2)
        population.append(child1)
        population.append(child2)
        population = sorted(population, key=fitness_function, reverse=True)[:len(population) - 2]
        best_number = max(population, key=fitness_function)
        print(f"Generation {generation + 1}: ",end = " ")
        print(f"Best Number = {best_number}, Fitness = {fitness_function(best_number)}")
        if best_number == 99999999:
            print(f"Converged at Generation {generation + 1}")
            break
    best_number = max(population, key=fitness_function)
    return best_number, fitness_function(best_number)

if __name__ == "__main__":
    population = [12345678, 87654321, 23456789, 98765432, 34567890, 45678901]
    generations = 22
    best_number, best_fitness = genetic_algorithm(population, generations)
    print(f"\nHighest 8-digit number: {best_number}, Fitness Score: {best_fitness}")
'''
Output:
Generation 1: Best Number = 98765889, Fitness = 60
Generation 2: Best Number = 98765889, Fitness = 60
Generation 3: Best Number = 98766889, Fitness = 61
Generation 4: Best Number = 98796889, Fitness = 64
Generation 5: Best Number = 98796889, Fitness = 64
Generation 6: Best Number = 98996889, Fitness = 66
Generation 7: Best Number = 98998889, Fitness = 68
Generation 8: Best Number = 98998889, Fitness = 68
Generation 9: Best Number = 98998889, Fitness = 68
Generation 10: Best Number = 98999999, Fitness = 71
Generation 11: Best Number = 98999999, Fitness = 71
Generation 12: Best Number = 99999999, Fitness = 72
Converged at Generation 12

Highest 8-digit number: 99999999, Fitness Score: 72
'''
