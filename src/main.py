from hashlib import new
import LDP
import Analyze
import csv

def ConnectParams(f,q,p):
    return "f=" + str(f) + ",q=" + str(q) + ",p=" + str(p)

#Parameter Setting
k = 10
m = 100
salts = [str(i) for i in range(k)]
"""
f: a probability for randamization (keep almost the original BF)
q: randomization of 1s in BF (q=1 -> keep 1, q=0 -> reversed to 0)
p: randomization of 1s in BF (p=1 -> reversed to 1, p=0 -> keep 0)
"""
f = 0.1
q = 0.9
p = 0.1
skipindex = [1]
openfile = r"data/wdbc.csv"
createfile = r"data/LDPfile(" + ConnectParams(f,q,p) + ").csv" 
analyzefile = r"data/wdbc(" + ConnectParams(f,q,p) + ").csv"

#Step1: input all items in csv onto a LDP protocol
with open(openfile) as file:
    reader = csv.reader(file)
    rowset = [row for row in reader]
LDPset = []
for row in rowset:
    newrow = []
    for i in range(len(row)):
        if i in skipindex:
            newrow.append(row[i])
            continue    
        #Construction BF
        BF = LDP.BloomFilter(k,m,salts)
        BF.setBF(str(row[i])) 
        S = LDP.LDP(BF,f,q,p)
        #convert a LDP output (array) to one string
        newitem = "".join(list(map(str,S)))
        newrow.append(float(newitem))
    LDPset.append(newrow)
    
#Step2: Save LDP's outputs as a csv file
with open(createfile, 'w',newline="") as file:
    writer = csv.writer(file)
    writer.writerows(LDPset)

#Step3: Analyze a csv made by LDP's output
Analyze.Analyze(createfile,analyzefile)