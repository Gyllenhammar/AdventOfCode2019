import math

try:
  file = open("day1_input.txt", "r")
except IOError:
  print("Error: Can't open file")
  import sys
  sys.exit(0)

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

file.close
print(totFuel)

