with open('input.txt','r') as f:
    data=f.read().splitlines()

data=[int(i) for i in data]

prev=[set() for _ in range(25)]
for i in range(25):
    for j in range(i):
        prev[j].add(data[j]+data[i])
        
for i,d in enumerate(data[25:],25):
    f=False
    for s in prev:
        f|=(d in s)
    if not f:
        print(d)
        break
    for j in range(25):
        prev[j].add(data[i-25+j]+d)
    prev.pop(0)
    prev.append(set())
