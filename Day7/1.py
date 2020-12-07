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
        adj[s[2:]].append(v)

c='shiny gold'
visited=set()
def dfs(color):
    visited.add(color)
    for a in adj[color]:
        dfs(a)
dfs(c)
print(len(visited)-1)
