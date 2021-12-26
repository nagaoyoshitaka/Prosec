import math
"""
import matplotlib.pyplot as plt
import csv

openfile = r"../data/wdbc.csv"
with open(openfile) as file:
    reader = csv.reader(file)
    rowset = [row for row in reader]
attr = []
n = len(rowset[0])
result = [[] for i in range(n)]
for row in rowset:
    for i in range(n):
        result[i].append(row[i])
plt.hist(result[22],bins = 25)
plt.show()
"""
"""
a = 0b111011111
b = 0b111111101

def euclid(a,b):
    r = 1
    while r!=0:
        r = a%b
        a = b
        b = r
        print(1)
    return a
"""

for i in range(13):
    print((i**2)%13)
print("---------------------")
for a in range(1,13):
    cnt = 0
    for x in range(13):
        y2 = (x**3+a*x)%13
        if y2 in [1,4,9,3,10,12]:
            cnt += 2
        elif x == 0:
            cnt += 0
    print(cnt)
