import copy

def readFile(inFile):
    stacks = []
    moves = []
    stacksOrMoves = 0
    with open(inFile, 'r') as file:
        for line in file:
            line.strip()
            # Constructing the stacks
            if not stacksOrMoves:    
                for i in range(len(line)//4):
                    if len(stacks)<i+1:
                        stacks.append([])
                    if (line[4*i+1] != ' '):
                        stacks[i].insert(0, line[4*i+1])
            # Constructing move list
            if stacksOrMoves:
                splitLine = line.split(" ")
                move = {"move":int(splitLine[1]), "from":int(splitLine[3])-1, "to":int(splitLine[5])-1}
                moves.append(move)
            if line == "\n":
                
                stacksOrMoves = 1
        # Stripping index from stack 
        for stack in stacks:
            stack.pop(0)
        
    return stacks, moves


def part1(stacks, moves):
    for move in moves:
        blocks = stacks[move["from"]][-move["move"]:]
        stacks[move["from"]] = stacks[move["from"]][:-move["move"]]
        stacks[move["to"]] += blocks[::-1]
    
    result = ''
    for stack in stacks:
        result+=stack[-1]
    print ("Part 1: ", result)

def part2(stacks, moves):
    for move in moves:
        blocks = stacks[move['from']][-move["move"]:]
        stacks[move["to"]] += blocks
        stacks[move["from"]] = stacks[move["from"]][:-move["move"]]
        
    result = ''
    for stack in stacks:
        result+=stack[-1]
    print ("Part 2: ", result)

if __name__ =="__main__":
    # inStacks, inMoves = readFile("testIn.txt")
    inStacks, inMoves = readFile("input.txt")
    part1(copy.deepcopy(inStacks), inMoves)
    part2(copy.deepcopy(inStacks), inMoves)