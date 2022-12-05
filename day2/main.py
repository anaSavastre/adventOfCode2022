
# from ..library import adventOfCodeFunctions as aocFn

def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            list.append(line.replace("\n", ""))
    return list
    
def partOne(input):
    shapePoints = {"rock":1, "scissors":3, "paper":2}
    elfShape = {letter : shape for letter, shape in zip("ABC", ["rock", "paper", "scissors"])}
    myShape = {letter : shape for letter, shape in zip("XYZ", ["rock", "paper", "scissors"])}

    points = {"draw":3, "lose":0, "win":6}
    wins = ["draw", "lose", "win"]
    shapeValue = {"rock":2, "scissors":1, "paper":0}
    
    # The order in which the game goes is rock>scissors>paper>rock (this is a cycle)
    # The result of the will be the diff in index shapes 
    # RP = 0 - 1 = -1 => points.keys[-1] = win (paper wins over rock)
    totalScore = 0
    for round in input:
        p1, p2 = round.split(" ")
        score = shapePoints[myShape[p2]]
        result = shapeValue[elfShape[p1]] - shapeValue[myShape[p2]]
        score += points[wins[result]]
        
        totalScore+=score
    return totalScore

def partTwo(input, debug=True):
    shapePoints = {"rock":1, "scissors":3, "paper":2}
    elfShape = {letter : shape for letter, shape in zip("ABC", ["rock", "paper", "scissors"])}
    resultLetter = {letter : shape for letter, shape in zip("XYZ", ["lose", "draw", "win"])}
    points = {"draw":3, "lose":0, "win":6}

    # My data
    wins = ["draw", "lose", "win"]
    shapeValue = ["paper", "scissors", "rock"]
    
    # The order in which the game goes is rock>scissors>paper>rock (this is a cycle)
    # The result of the will be the diff in index shapes 
    # RP = 0 - 1 = -1 => points.keys[-1] = win (paper wins over rock)
    totalScore = 0
    for round in input:
        p1, result = round.split(" ")
        score = points[resultLetter[result]]
        # mShape = p1Shape - resultIndex
        # print([elfShape[p1]])
        mShape = shapeValue.index(elfShape[p1]) - wins.index(resultLetter[result])
        score += shapePoints[shapeValue[mShape]]
        
        # print(shapeValue[mShape])
        totalScore+=score
    return totalScore


if __name__ =="__main__":
    input = readFile("input.txt")
    rez = partOne(input)
    print("Part 1:", rez)

    rez = partTwo(input)
    print("Part 2:", rez)
