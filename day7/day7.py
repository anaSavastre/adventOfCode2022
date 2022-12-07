class fileStruct:
    def __init__(self, size, name, path):
        self.size = size
        self.name = name
        self.path = path
class directoryStructure:
    def __init__(self, path, size, name, children=None):
        self.path = path
        self.size = size
        self.name = name
        self.children = children


def readFile(inFile):
    files = {}
    directories = {}
    path = []
    with open(inFile, 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            if ("$ cd" in line):
                if (".." in line):
                    path.pop()
                    continue
                dir = directoryStructure('/'.join(path), 0, line[5:])
                path.append(line[5:])
                directories['/'.join(path)] = dir
                continue
            if ("$ ls" in line):
                continue
            if ("dir" in line):
                continue
            size, name = line.split(" ")
            files['/'.join(path+[name])] = fileStruct(int(size), name, '/'.join(path))

    return directories, files

def computeSizes(files, directories):
    for path in files.keys():
        value = files[path].size
        while(path!='/'):
            if path in directories.keys():
                path = directories[path].path
            else:
                path = files[path].path
            directories[path].size += value
    
    # for path in directories.keys():
    #     print(path, directories[path].size)
    
    
def partOne(directories):
    sum = 0 
    for path, directory in directories.items():
        if  directory.size <= 100000:
            sum+=directory.size
    print("PART 1: ", sum)

def partTwo(directories):
    totalSpace = 70000000
    freeSpace = totalSpace - directories['/'].size
    needToFree = 30000000 - freeSpace
    minSpaceToFree = directories['/'].size
    for path, d in directories.items():
        if d.size > needToFree and d.size < minSpaceToFree:
            minSpaceToFree = d.size
    
    print("PART 2: ", minSpaceToFree)

if __name__ =="__main__":
    # dirs, files = readFile("testIn.txt")
    dirs, files = readFile("input.txt")
    computeSizes(files, dirs)

    partOne(dirs)
    partTwo(dirs)