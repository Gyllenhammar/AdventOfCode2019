import math

try:
  file = open("day1_input.txt", "r")
except IOError:
  print("Error: Can't open file")
  import sys
  sys.exit(0)

def calculateFuel(mass):
  return math.floor(int(mass)/3) - 2


def calcFuelNeeded(mass):
    fuelNeeded = 0
    fuelNeeded += calculateFuel(mass)
    if (fuelNeeded > 0):
        fuelNeeded +=  int(calcFuelNeeded(fuelNeeded))
        return fuelNeeded
    else:
        return 0

totFuel = 0
for line in file:
    totFuel += calcFuelNeeded(int(line))

file.close
print(totFuel)

