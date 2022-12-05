def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            line = line.replace("\n", "") 
            list.append(line)
    return list

def partOne(input):
    priority = [chr(letter) for letter in range(ord("a"), ord("z")+1)] + [chr(letter) for letter in range(ord("A"), ord("Z")+1)]

    prioritySum=0
    for rucksack in input:
        length = len(rucksack)
        comp1 = set(rucksack[:length//2])
        comp2 = set(rucksack[length//2:])

        commonElem = comp1.intersection(comp2) 
        for elem in list(commonElem):
            prioritySum += priority.index(elem)+1
    print("Part 1: ", prioritySum)

def partTwo(input):
    priority = [chr(letter) for letter in range(ord("a"), ord("z")+1)] + [chr(letter) for letter in range(ord("A"), ord("Z")+1)]

    prioritySum=0
    # Common element in every 3 rucksacks
    for index in range(len(input)//3):
        rucksacks = input[index*3: index*3+3]
        badge = set(rucksacks[0])
        for j in range(2):
            badge = badge.intersection(set(rucksacks[j+1]))
        prioritySum += priority.index(list(badge)[0])+1

    print("Part 2: ", prioritySum)

if __name__ =="__main__":
    # input = readFile("testIn.txt")
    input = readFile("in.txt")
    partOne(input)
    partTwo(input)