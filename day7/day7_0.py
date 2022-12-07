from importlib.resources import files


class fileStruct:
    def __init__(self, name, size, type, path):
        self.size = size
        self.type = type
        self.path = path
        self.name = name

def readFile(inFile):
    fileGraph = {'/':fileStruct("/", 0, "dir", None)}
    graphChildren = []
    curentDir = []
    with open(inFile, 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            if 'cd' in line:
                if '..' in line:
                    curentDir.pop()
                    continue
                curentDir.append(line[5:])
                if '/'.join(curentDir) not in fileGraph.keys():
                    fileGraph['/'.join(curentDir)] = fileStruct(line[5:], 0, "dir", '/'.join(curentDir[:-1]))
                continue
            if line == "$ ls":
                continue
            # Adding the file to the struct
            splitLine = line.split(" ")
            type = "dir" if splitLine[0] == "dir" else "file" 
            size =  0 if splitLine[0] == "dir" else int(splitLine[0])
            filePath = '/'.join(curentDir+[splitLine[1]])
            fileGraph[filePath] = fileStruct(splitLine[1], size, type, '/'.join(curentDir))
    return fileGraph

def computeFileSizes(fileGraph: dict):
    # We want to complete the sizes of the files 
    filePaths = [key for key in fileGraph.keys() if fileGraph[key].type=="file"]
    for path in filePaths:
        value = fileGraph[path].size
        while(path!="/"):
            path = fileGraph[path].path
            fileGraph[path].size += value
    
    # for path in fileGraph.keys():
    #     print(path, fileGraph[path].size)

    return fileGraph

def partOne(fileGraph:dict):
    sum = 0
    for path in fileGraph:
        if  fileGraph[path].size <= 100000 and fileGraph[path].type=="dir":
            sum+=fileGraph[path].size
    print("Part 1: ", sum)

if __name__ =="__main__":
    # input = readFile("testIn.txt")
    input = readFile("input.txt")
    
    newIn = computeFileSizes(input)

    partOne(newIn)
    # partTwo(input)