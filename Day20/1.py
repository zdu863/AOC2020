from collections import Counter

with open('input.txt','r') as f:
    data=f.read().splitlines()

maps={}
i=0
while i<len(data):
    num=int(data[i][5:9])
    maps[num]=[]
    while True:
        i+=1
        if i==len(data) or not data[i]:
            break
        maps[num].append(data[i])
    i+=1

edges={}
for num,m in maps.items():
    t,b,l,r=m[0],m[-1],''.join(r[0] for r in m),''.join(r[-1] for r in m)
    tf,bf,lf,rf=t[::-1],b[::-1],l[::-1],r[::-1]
    for e in [t,b,l,r,tf,bf,lf,rf]:
        if e in edges:
            edges.pop(e)
        else:
            edges[e]=num
            
ans=1
for k,v in Counter(edges.values()).items():
    if v==4:
        ans*=k
print(ans)
