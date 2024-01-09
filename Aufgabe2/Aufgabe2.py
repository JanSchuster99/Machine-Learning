import numpy
import random
import math
import matplotlib.pyplot as plt


def generate2DArray(n):
    # initialize a empty two dimesional array
    table = numpy.empty(shape=(n,n), dtype=int)
    
    # fill the two dimensional array with random numbers between 1 and 9
    for i in range(0,n):
        for j in range(0,n):
            if(i == j):
                table[i][j] = 0
            else:
                temp = random.randint(1,50)
                table[i][j] = temp
                table[j][i] = temp
    return table

# calculate the fitness of a route
def calcFit(route, cityTable):
    fitness = 0
    
    for i in range(0, len(route)):
        fitness -= cityTable[route[i]][route[(i+1)%len(route)]]
       
    return fitness

def hillClimber(route, cityTable):
    bestRoute = route
    fitOfBestRoute = calcFit(route, cityTable)
    temperature = 10
    epsilon = 0.001
    fitnessValues = []
    
    while(temperature > epsilon):
        # swap two random Citys in the bestRoute array
        randCity1 = random.randint(0, len(route)-1)
        randCity2 = random.randint(0, len(route)-1)
        bestRoute[randCity1], bestRoute[randCity2] = bestRoute[randCity2], bestRoute[randCity1]
        
        # calculate the fitness for the new route
        fitOfCurrRoute = calcFit(bestRoute, cityTable)

        fitChange = fitOfCurrRoute - fitOfBestRoute
        
        # if the current fitness is better than the old one, the current Route is now the best Route
        if fitChange > 0:
            fitOfBestRoute = fitOfCurrRoute
            fitnessValues.append(fitOfBestRoute)
            #print(bestRoute, fitOfBestRoute)
            print("Step forward: {}".format(fitOfBestRoute))

        else:
            
            acceptProb = math.exp(fitChange / temperature)
            if random.random() < acceptProb and acceptProb != 1:
                fitOfBestRoute = fitOfCurrRoute
                fitnessValues.append(fitOfBestRoute)
                print("Step backwards: {} {}".format(fitOfBestRoute, acceptProb))
        
            # if the old Route has still the best fitness, the citys are swapped back
            else:
                #print("No Step")
                bestRoute[randCity1], bestRoute[randCity2] = bestRoute[randCity2], bestRoute[randCity1]

        temperature = temperature - epsilon
    return fitnessValues
    

n=100
route = []
for i in range(0, n):
    route.append(i)
cityTable = generate2DArray(n)   
print("Distance table:")
print(numpy.matrix(cityTable)) 
iniRoute = calcFit(route, cityTable)
print(calcFit(route, cityTable))
print("Optimizations of fitness:")
fitnessValues = hillClimber(route, cityTable)
print("Initial route fitness:")
print(iniRoute)

plt.plot(fitnessValues)
plt.xlabel("Iteration")
plt.ylabel("Fitness Value")
plt.title("Fitness Value over Iterations")
plt.show()