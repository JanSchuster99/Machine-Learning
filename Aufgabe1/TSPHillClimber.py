import numpy
import random
def generateJourney(n):
    journey = numpy.empty(shape=n, dtype='object')
    for i in range(0,n):
        journey[i] = i
    return journey
        
def generateArray(n):
    cityTable = numpy.zeros(shape=(n,n), dtype='object')
    for i in range(0, n):
        for j in range(i+1, n):
                temp = random.randint(1,9)
                cityTable[i][j] = temp
                cityTable[j][i] = temp

    return cityTable

def journeylength(journey, table):
    journeyValue = 0
    for i in range(0, len(journey)):
        journeyValue += table[journey[i], journey[(i-1)]]
    return journeyValue

def hillClimber(table, journey):
    iterations = 10**5
    lastJourney = journey
    lastJourneyLength = journeylength(lastJourney, table)
    for i in range(0, iterations):
        counter = 0
        rand1 = random.randint(0,len(journey)-1)
        rand2 = random.randint(0,len(journey)-1)
        lastJourney[rand1], lastJourney[rand2] = lastJourney[rand2], lastJourney[rand1] #swaps 2 random indices in journey array
        if lastJourneyLength > journeylength(lastJourney, table): 
            lastJourneyLength = journeylength(lastJourney, table) 
            counter = 0 #save new journey length if shorter
        else: 
            lastJourney[rand1], lastJourney[rand2] = lastJourney[rand2], lastJourney[rand1]
            counter +=1#swap back if new journey isnt better
            if counter > 1000:
                break
    return (lastJourney, lastJourneyLength)


JOURNEYLENGTH = 100
MAPSIZE = 100
table = generateArray(MAPSIZE)
journey = generateJourney(JOURNEYLENGTH)
print(table)
print(journey, journeylength(journey, table))
print(hillClimber(table,journey))# -*- coding: utf-8 -*-

