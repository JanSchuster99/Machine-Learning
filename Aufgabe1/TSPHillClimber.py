import numpy
import random

def generateArray(n):
    cityTable = numpy.empty(shape=(n,n), dtype='object')
    for i in range(0, n):
        for j in range(0, n):
            if(j == i):
                cityTable[i][j] = 0
            else: 
                temp = random.randint(1,9)
                cityTable[i][j] = temp
                cityTable[j][i] = temp

    return cityTable
def journeylength(journey, table):
    journeyValue = 0
    for i in range(0, len(journey)-1):
        journeyValue += table[journey[i], journey[i+1]]
    return journeyValue

def hillClimber(table, journey):
    iterations = 10**6
    lastJourney = journey
    lastJourneyLength = journeylength(lastJourney, table)
    for i in range(0, iterations):
        rand1 = random.randint(0,len(journey)-1)
        rand2 = random.randint(0,len(journey)-1)
        lastJourney[rand1], lastJourney[rand2] = lastJourney[rand2], lastJourney[rand1] #swaps 2 random indices in journey array
        if lastJourneyLength > journeylength(lastJourney, table): 
            lastJourneyLength = journeylength(lastJourney, table) #save new journey length if shorter
        else: 
            lastJourney[rand1], lastJourney[rand2] = lastJourney[rand2], lastJourney[rand1] #swap back if new journey isnt better
    return (lastJourney, lastJourneyLength)



table = generateArray(5)
journey = [0,2,4,1,3]
print(table)
print(journey, journeylength(journey, table))
print(hillClimber(table,journey))

