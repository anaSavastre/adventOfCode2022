
def readFile(inFile):
    list=[]
    with open(inFile, 'r') as file:
        for line in file:
            list = line.replace("\n", "")
    return list

def messageMarker(message, markerLength=4):
    for i, character in enumerate(message):
        # Break if we are at the end of string 
        if (i>len(message)-markerLength):
            return
        # Check if we foound the marker
        marker = message[i:i+markerLength] 
        if (len(marker) == len(set(marker))):
            return i+markerLength

def partOne(input):
    marker = messageMarker(input, 4)
    print("Part 1: ", marker)

def partTwo(input):
    marker = messageMarker(input, 14)
    print("Part 2: ", marker)

if __name__ =="__main__":
    # input = readFile("testIn.txt")
    input = readFile("input.txt")

    partOne(input)
    partTwo(input)