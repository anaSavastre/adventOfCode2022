def partOne(inFile):
    sums=[0]
    index=0
    with open(inFile, 'r') as file:
        for line in file:
            # list.append(int(line))
            if line == "\n":
                index+=1
                sums.append(0)
                continue
            sums[index]+=int(line)
    print("Part 1: ", max(sums))
    return list

def partTwo(inFile):
    sums=[0]
    index=0
    with open(inFile, 'r') as file:
        for line in file:
            # list.append(int(line))
            if line == "\n":
                index+=1
                sums.append(0)
                continue
            sums[index]+=int(line)
    sums = sorted(sums)
    print(sum(sums[-3:]))
    return list
if __name__ =="__main__":
    # partOne("input.txt")
    partTwo("input.txt")