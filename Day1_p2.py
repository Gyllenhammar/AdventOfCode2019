import math

file = open("day1.txt", "r")

def calculateFuel(mass):
    fuelNeeded = 0
    fuelNeeded += math.floor(int(mass)/3) - 2
    if (fuelNeeded > 0):
        fuelNeeded +=  int(calculateFuel(fuelNeeded))
        return fuelNeeded
    else:
        return 0

totFuel = 0
for line in file:
    totFuel += calculateFuel(int(line))
print(totFuel)

