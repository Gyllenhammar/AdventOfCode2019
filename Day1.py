import math

file = open("day1.txt", "r")

fuel = 0
for line in file:
  fuel = fuel + math.floor(int(line)/3) - 2
print(fuel)