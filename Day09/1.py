from itertools import combinations

with open('input.txt','r') as f:
    data=f.read().splitlines()

data=[int(i) for i in data]

for i in range(25,len(data)):
    s=set(a+b for a,b in combinations(data[i-25:i],2))
    if data[i] not in s:
        print(data[i])
        break
