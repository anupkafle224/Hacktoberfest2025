import random

# ---- Problem setup ----
# We will maximize f(x) = x^2, where x is an integer between -100 and 100.

def fitness(x):
    """Fitness function: higher is better."""
    return x**2

# ---- Genetic Algorithm ----
def genetic_algorithm(
    population_size=20, generations=50, mutation_rate=0.1, crossover_rate=0.8,
    lower_bound=-100, upper_bound=100
):
    # Initialize random population
    population = [random.randint(lower_bound, upper_bound) for _ in range(population_size)]
    
    for gen in range(generations):
        # Calculate fitness for each individual
        fitness_scores = [fitness(ind) for ind in population]
        
        # Select parents (roulette-wheel selection)
        total_fitness = sum(fitness_scores)
        if total_fitness == 0:
            total_fitness = 1
        selection_probs = [f/total_fitness for f in fitness_scores]

        # Create next generation
        new_population = []
        for _ in range(population_size // 2):
            # Select two parents
            parents = random.choices(population, weights=selection_probs, k=2)
            parent1, parent2 = parents[0], parents[1]

            # Crossover
            if random.random() < crossover_rate:
                # Single-point crossover
                point = random.randint(1, 31)  # use bit-level crossover
                mask = (1 << point) - 1
                child1 = (parent1 & mask) | (parent2 & ~mask)
                child2 = (parent2 & mask) | (parent1 & ~mask)
            else:
                child1, child2 = parent1, parent2

            # Mutation
            if random.random() < mutation_rate:
                child1 += random.randint(-3, 3)
            if random.random() < mutation_rate:
                child2 += random.randint(-3, 3)

            # Keep children within bounds
            child1 = max(min(child1, upper_bound), lower_bound)
            child2 = max(min(child2, upper_bound), lower_bound)

            new_population.extend([child1, child2])

        population = new_population

        # Track best individual in this generation
        best_idx = fitness_scores.index(max(fitness_scores))
        print(f"Generation {gen+1}: Best = {population[best_idx]}, Fitness = {fitness_scores[best_idx]}")

    # Return best overall
    fitness_scores = [fitness(ind) for ind in population]
    best_idx = fitness_scores.index(max(fitness_scores))
    return population[best_idx], fitness_scores[best_idx]

# ---- Run GA ----
best_solution, best_fitness = genetic_algorithm()
print("\nBest solution found:", best_solution)
print("Fitness:", best_fitness)
