
try:
  file = open("Day3_input.txt", "r")
except IOError:
  print("Error: Can't open file")
  import sys
  sys.exit(0)

def process_wire(wire):
    currCoord = [0,0]
    for command in wire.split(","):
        for _ in range(int(command[1:])):
            opCode = command[0]
            if opCode == 'U':
                currCoord = [currCoord[0], currCoord[1] + 1]
            elif opCode == 'R':
                currCoord = [currCoord[0] + 1, currCoord[1]]
            elif opCode == 'D':
                currCoord = [currCoord[0], currCoord[1] - 1]
            elif opCode == 'L':
                currCoord = [currCoord[0] - 1, currCoord[1]]
           
            yield tuple(currCoord)

def findClosestCrossing(crossings, origin):
    Shortestpath = 0
    for crossing in crossings:
        path = abs(crossing[0] - origin[0]) + abs(crossing[1] - origin[1])
        if path < Shortestpath or Shortestpath == 0:
            Shortestpath = path
    return Shortestpath

wires = []    
for wire in file.readlines():
    wires += [list(process_wire(wire))]
file.close

crossings = (set(wires[0]) & set(wires[1]))
print(findClosestCrossing(crossings,(0,0)))

    