with open('input.txt','r') as f:
    data=f.read().splitlines()

fields=[]
constrains=[]
for line in data[:20]:
    name,tmp=line.split(':')
    fields.append(name)
    ct=[]
    for s in tmp.split('or'):
        ct.append([int(c) for c in s.strip().split('-')])
    constrains.append(ct)

discard=set()
for i,line in enumerate(data[25:]):
    vals=[int(a) for a in line.split(',')]
    for v in vals:
        valid=False
        for k,ct in enumerate(constrains):
            for l,h in ct:
                if l<=v<=h:
                    valid=True
            if valid:
                break
        if not valid:
            discard.add(i)
            break

possible=[{i for i in range(20)} for _ in range(20)]
for i,line in enumerate(data[25:]):
    if i in discard:
        continue
    vals=[int(a) for a in line.split(',')]
    for j,v in enumerate(vals):
        tmp=set()
        for k,ct in enumerate(constrains):
            for l,h in ct:
                if l<=v<=h:
                    tmp.add(k)
        possible[j]&=tmp
        
possible=sorted([[i,p] for i,p in enumerate(possible)],key=lambda x: len(x[1]))
d={}
for i,s in possible:
    if len(s)==1:
        d[s.pop()]=i
        continue
    for v in s:
        if v in d:
            continue
        d[v]=i
        break
ans=1 
ticket=[89,179,173,167,157,127,163,113,137,109,151,131,97,149,107,83,79,139,59,53]
for i in range(6):
    ans*=ticket[d[i]]  
print(ans) 
