import matplotlib.pyplot as plt
import numpy as np
sackCapacity = 100  
numGifts = 100
populationSize = 1000
generations = 50
mutationRate = 0.01

# assigning random values to gifts
giftVolumes = np.random.uniform(0.1, 2.0, numGifts)

# Initialize random genes
population = np.random.choice([0, 1], size=(populationSize, numGifts))

def fitness(genes):
    totalVolume = np.sum(genes * giftVolumes)
    return 1 / (abs(sackCapacity - totalVolume) + 1)

bestVolumes = []

for generation in range(generations):
    # Calc Fitness for every gene combination in population
    fitnessScores = np.array([fitness(genes) for genes in population])

    # Picking best individuals based on fitness
    selectedIndices = np.argsort(fitnessScores)[-populationSize // 2:]
    selectedPopulation = population[selectedIndices]

    # Crossover
    crossoverPoint = np.random.randint(1, numGifts)
    offspring = np.concatenate(
        (selectedPopulation[:, :crossoverPoint], selectedPopulation[:, crossoverPoint:]),
        axis=1
    )


    # replace old Population with selected population and offspring
    population[:populationSize // 2] = selectedPopulation
    population[populationSize // 2:] = offspring

    # Mutation
    mutationMask = np.random.rand(*population.shape) < mutationRate
    population[mutationMask] = 1 - population[mutationMask]

    # Final Evaluation and Choice of best indivual
    finalFitness = np.array([fitness(genes) for genes in population])
    bestIndivualIndex = np.argmax(finalFitness)
    bestIndividual = population[bestIndivualIndex]

    # Collect Volume of best this generation
    totalVolumePacked = np.sum(bestIndividual * giftVolumes)
    bestVolumes.append(totalVolumePacked)

    # Print results
    print(f"Generation {generation + 1}: {totalVolumePacked:.2f} Liter")


plt.plot(bestVolumes)
plt.title('Evolution of best Sack per generation')
plt.xlabel('Generation')
plt.ylabel('Volume of sack in liter')
plt.show()