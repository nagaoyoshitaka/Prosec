import random
import hashlib
import matplotlib.pyplot as plt
"""
input: probability p (int only >= 0.001)
output: 1 with a probability p, else 0
"""
def mCoin(p):
    acc = 10000
    r = random.randint(1,acc)
    if r <= acc*p:
        return 1
    else:
        return 0

"""
input: nothing
output: 1 with a probability 1/2, else 0
"""
def coin():
    r = random.randint(0,1)
    return r

class BloomFilter:
    
    """
    Patameters
    k: the number of hash functions
    m: the length of BloomFilter
    salts: used for constructiong different BloomFilter each times
    """
    def __init__(self, k, m, salts):
        self.salts = salts
        self.m = m
        self.k = k
        self.BF = [0 for i in range(m)]
    
    """
    Parameters
    i: an index of hash function
    s: input message
    """
    def hash(self, i, s):
        d = (self.salts[i] + s).encode()
        b = hashlib.sha256(d).hexdigest()
        v = int('0x' + b,16)
        return v % self.m
        
    #input an item s onto BF
    def setBF(self,s):
        for i in range(self.k):
            index = self.hash(i,s)
            self.BF[index] = 1
        assert self.checkBF(s) == 1
    
    #input items s=[s1,...,sn] onto BF
    def manySetBF(self,s):
        for si in s:
            self.setBF(si)
        
    #output 1 if s is in BF
    def checkBF(self,s):
        for i in range(self.k):
            index = self.hash(i,s)
            if self.BF[index] != 1:
                return 0
        return 1

def LDP(BloomFilter,f,q,p):
    #step2 (in the paper)
    subBF= BloomFilter.BF.copy()
    for i in range(BloomFilter.m):
        r = mCoin(f)
        if r == 1:
            b = coin()
            if b == 0:
                subBF[i] = 1
            else:
                subBF[i] = 0
    #step3 (in the paper)
    S = [0 for i in range(BloomFilter.m)]
    for i in range(BloomFilter.m):
        if subBF[i] == 1:
            S[i] = mCoin(q)
        else:
            S[i] = mCoin(p)
    #display each sets
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(10,5))
    showSomeSet("Bloom FIlter", BF.BF,ax1)
    showSomeSet("Bloom Filter'",subBF ,ax2)
    showSomeSet("LDP",S ,ax3)
    fig.show
    fig.savefig("output/LDP.png")
    return S 

#display someset by using a bar graph
def showSomeSet(title, someset, plot):
    x = [i for i in range(len(someset))]
    plot.bar(x, someset)
    plot.set_title(title)

def BFtest(BF, checkItems):
    for item in checkItems:
        BF.checkBF(item) 
    
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
q = 0.8
p = 0.2
#Construction BF
BF = BloomFilter(k,m,salts)
BF.setBF("a") 
print("---Check LDP---")
S = LDP(BF,0.2,q,p)
#If you want to use LDP's output, use the following S:
#print("---LDP Protocol's output---")
#show a raw LDP output
#print(S)
#show a LDP output in one string
print("".join(list(map(str,S))))