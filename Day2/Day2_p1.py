
try:
  file = open("Day2_input.txt", "r")
except IOError:
  print("Error: Can't open file")
  import sys
  sys.exit(0)

lines = file.read().split(',')
file.close
lines = [int(i) for i in lines]

lines[1] = 12
lines[2] = 2

def runProgram(program):
    pos = 0
    while program[pos] != 99:
        if (program[pos] == 1):
            program = op1(program,pos)
        elif(program[pos] == 2):
            program = op2(program,pos)
        pos += 4
    return program

def op1(list, pos):
    list[list[pos+3]] = list[list[pos+1]] + list[list[pos+2]]
    return list

def op2(list, pos):
    list[list[pos+3]] = list[list[pos+1]] * list[list[pos+2]]
    return list

print(runProgram(lines))





