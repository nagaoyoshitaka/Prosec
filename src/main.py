import LDP

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
BF = LDP.BloomFilter(k,m,salts)
BF.setBF("a") 
print("---Check LDP---")
S = LDP.LDP(BF,0.2,q,p)
#If you want to use LDP's output, use the following S:
#print("---LDP Protocol's output---")
#show a raw LDP output
#print(S)
#show a LDP output in one string
print("".join(list(map(str,S))))