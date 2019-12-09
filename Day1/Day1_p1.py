import math


file = open("Day1_input.txt", "r")


def calculateFuel(mass):
  return int(math.floor(int(mass)/3) - 2)

fuel = 0
for line in file:
  fuel += calculateFuel

file.close
print(fuel)