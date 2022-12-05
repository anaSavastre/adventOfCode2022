from operator import truediv


class interval:
    def __init__(self, list):
        self.min1 = int(list[0][0])
        self.max1 = int(list[0][1])
        self.min2 = int(list[1][0])
        self.max2 = int(list[1][1])

    def containment(self):
        '''
        min1 min2 max2 max1
        or
        min2 min1 max1 max2
        '''
        if (self.min1 <= self.min2) and (self.max2 <= self.max1):
            return True
        if (self.min2 <= self.min1) and (self.max1 <= self.max2):
            return True
        return False

    def overlap(self):
        '''
        min1 min2 max1 max2
        min2 min1 max2 max1
        '''
        if (self.min1<=self.min2<=self.max1) or (self.min1<=self.max2<=self.max1):
            return True
        if (self.min2<=self.min1<=self.max2) or (self.min2<=self.max1<=self.max2):
            return True
        return False

def readFile(inFile):
    elfPairs = []
    with open(inFile, 'r') as file:
        for line in file:
            line = line.replace("\n", "") 
            elfs = [elem.split("-") for elem in line.split(",")]
            elfPairs.append(interval(elfs))

    return elfPairs


def part1(input):
    overlapPairs = 0
    for pair in input:
        if pair.containment():
            overlapPairs += 1 
    print("Part 1: ", overlapPairs)


def part1(input):
    overlapPairs = 0
    for pair in input:
        if pair.overlap():
            overlapPairs += 1 
    print("Part 1: ", overlapPairs)

if __name__ =="__main__":
    # input = readFile("testIn.txt")
    input = readFile("input.txt")
    part1(input)

