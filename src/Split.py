import csv
import math
import numpy as np

#maxnum = BFlength
#split according to the same length of the entire range.
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
    midResult = []
    for i in range(n):
        if i in skipindex:
            result.append([])
            continue
        #define the number of split
        length = math.floor(maxset[i]-minset[i])
        flength = maxset[i]-minset[i]
        splitTupleSet = []
        midSet = []
        if length <= minnum:
            m = minset[i]
            M = maxset[i]
            d = flength/minnum
            for j in range(minnum):
                if j!= minnum-1:
                    splitTupleSet.append((m,m+d))
                    midSet.append((m+(d/2)))
                    m += d
                else:
                    splitTupleSet.append((m,M))
                    midSet.append((m+M)/2)
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
        midResult.append(midSet)
    return result, midResult

#split according to the same number of attributes.
def getSplitTupleSetForAttributes2(filename, skipindex,splitnum):
    with open(filename) as file:
        reader = csv.reader(file)
        rowset = [row for row in reader]
    n = len(rowset[0])
    l = len(rowset)
    attrset = [[] for i in range(n)]
    for row in rowset:
        for i in range(n):
            if i in skipindex:
                attrset[i].append(row[i])
            else:
                attrset[i].append(float(row[i]))
    result = []
    midResult = []
    for i in range(n):
        rangeset = []
        if i in skipindex:
            result.append([])
            continue
        sortedset = np.sort(attrset[i])
        midSet = []
        for j in range(splitnum):
            a = float(sortedset[int(l*j/splitnum)])
            b = float(sortedset[min(int(l*(j+1)/splitnum),l-1)])
            rangetuple = (a,b)
            midSet.append((a+b)/2)
            rangeset.append(rangetuple)
        result.append(rangeset)
        midResult.append(midSet)
    return result, midResult

def Label(item,tupleSet):
    for tuple in tupleSet:
        if tuple[0] <= float(item) and float(item) <=tuple[1]:
            return str(tuple[0]) + str(":") + str(tuple[1])
    return "error"

def Label2(item,tupleSet):
    cnt = 0
    for tuple in tupleSet:
        if tuple[0] <= float(item) and float(item) <=tuple[1]:
            return cnt
        cnt += 1
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
                labelset.append(Label2(row[i],splitTupleSetForAttributes[i]))
        result.append(labelset)
    with open(createfilename, 'w',newline="") as cfile:
        writer = csv.writer(cfile)
        writer.writerows(result)
    
    
