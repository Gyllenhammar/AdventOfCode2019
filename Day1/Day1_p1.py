import math

try:
  file = open("day1_input.txt", "r")
except IOError:
  print("Error: Can't open file")
  import sys
  sys.exit(0)

def calculateFuel(mass):
  return math.floor(int(mass)/3) - 2

fuel = 0
for line in file:
  fuel += calculateFuel(line)

file.close
print(fuel)