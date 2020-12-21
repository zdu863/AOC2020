with open('input.txt','r') as f:
    data=f.read().splitlines()

li,la=[],[]
s_ingr=set()
s_alle=set()

for line in data:
    line=line.replace('(','').replace(')','')
    ingr,alle=line.split('contains')
    ingr,alle=ingr.strip().split(),alle.strip().split(', ')
    s_ingr|=set(ingr)
    s_alle|=set(alle)
    li.append(ingr)
    la.append(alle)

d={a:set() for a in s_alle}  # ingredients that doesn't have a certain allegen
for a in s_alle:
    tmp=s_ingr.copy()
    for i,l in enumerate(la):
        if a not in l:
            continue
        ingi=set(li[i])
        d[a]|=tmp-ingi
        tmp&=ingi

no_alle=set.intersection(*d.values())

ans=0
for l in li:
    ans+=sum(i in no_alle for i in l)

print(ans)
        
            
            
