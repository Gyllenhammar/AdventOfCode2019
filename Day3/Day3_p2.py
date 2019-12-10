
try:
  file = open("Day3_input.txt", "r")
except IOError:
  print("Error: Can't open file")
  import sys
  sys.exit(0)

def findLowestCrossing(wires, crossings, origin):
    lowestCrossing = 0
    for crossing in crossings:
        tempdistance = 0
        for wire in wires:
            tempdistance += wire.index(crossing)
        if tempdistance < lowestCrossing or lowestCrossing == 0:
            lowestCrossing = tempdistance
    return lowestCrossing + 2

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

wires = []    
for wire in file.readlines():
    wires += [list(process_wire(wire))]
file.close


crossings = (set(wires[0]) & set(wires[1]))
print(findLowestCrossing(wires, crossings, (0,0)))    