import csv
import math

#maxnum = BFlength
def getSplitTupleSetForAttributes(filename, skipindex,minnum,maxnum):
    with open(filename) as file:
        reader = csv.reader(file)
        rowset = [row for row in reader]
    n = len(rowset[0])
    result = []
    minset = [float(100000) for i in range(n)]
    maxset = [float(0) for i in range(len(rowset[0]))]
    for row in rowset:
        for i in range(n):
            if i in skipindex:
                continue
            if float(row[i]) < minset[i]:
                minset[i] = float(row[i])
            if float(row[i]) > maxset[i]:
                maxset[i] = float(row[i])
    print(minset)
    print(maxset)
    for i in range(n):
        if i in skipindex:
            result.append([])
            continue
        #define the number of split
        length = math.floor(maxset[i]-minset[i])
        flength = maxset[i]-minset[i]
        splitTupleSet = []
        if length <= minnum:
            m = minset[i]
            M = maxset[i]
            d = flength/minnum
            for j in range(minnum):
                if j!= minnum-1:
                    splitTupleSet.append((m,m+d))
                    m += d
                else:
                    splitTupleSet.append((m,M))
        elif length > minnum:
            m = minset[i]
            M = maxset[i]
            num = min(length,maxnum)
            d = flength/float(num)
            for j in range(num):
                if j!= num-1:
                    splitTupleSet.append((m,m+d))
                    m += d
                else:
                    splitTupleSet.append((m,M))
        result.append(splitTupleSet)
    return result

def Label(item,tupleSet):
    for tuple in tupleSet:
        if tuple[0] <= float(item) and float(item) <=tuple[1]:
            return str(tuple[0]) + str(":") + str(tuple[1])
    return "error"

def makeLabeledFile(filename, createfilename,splitTupleSetForAttributes,skipindex):
    with open(filename) as file:
        reader = csv.reader(file)
        rowset = [row for row in reader]
    result = []
    for row in rowset:
        labelset = []
        for i in range(len(row)):
            if i in skipindex:
                labelset.append(row[i])
            else:
                labelset.append(Label(row[i],splitTupleSetForAttributes[i]))
        result.append(labelset)
    with open(createfilename, 'w',newline="") as cfile:
        writer = csv.writer(cfile)
        writer.writerows(result)
    
    
