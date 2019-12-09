
try:
  file = open("Day2_input.txt", "r")
except IOError:
  print("Error: Can't open file")
  import sys
  sys.exit(0)

lines = file.read().split(',')
file.close
initProgram = [int(i) for i in lines]

memory = []

def resetMemory():
    global memory
    memory = []

def loadProgram():
    global memory
    memory = list(initProgram)


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

def findNounVerb():
    global memory
    for noun in range(100):
        for verb in range(100):
            memory[1] = noun
            memory[2] = verb
            outputMemory = runProgram(memory)
            #print(outputMemory)
            if (outputMemory[0] == 19690720):
                print("Solution:")
                print(100*noun+verb)
                return
            resetMemory()
            loadProgram()


#Main
resetMemory()
loadProgram()
findNounVerb()

