import re
from collections import defaultdict
with open('input.txt','r') as f:
    data=f.read().splitlines()

adj=defaultdict(list)
for line in data:
    tmp=re.split('bags|bag',line.replace('contain','').replace(',',''))
    tmp=[s.strip() for s in tmp]
    
    v=tmp[0]
    for s in tmp[1:-1]:
        if s=='no other':
            continue
        adj[v].append((s[2:],int(s[0])))

c='shiny gold'
def nbags(color):
    ret=0
    for c,n in adj[color]:
        ret+=n*(1+nbags(c))
    return ret
    
print(nbags(c))
