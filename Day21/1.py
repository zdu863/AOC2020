with open('input.txt','r') as f:
    data=f.read().splitlines()

li,la=[],[]
s_ingr=set()
s_alle=set()

for line in data:
    line=line.replace('(','').replace(')','')
    ingr,alle=line.split('contains')
    ingr,alle=set(ingr.strip().split()),set(alle.strip().split(', '))
    s_ingr|=ingr
    s_alle|=alle
    li.append(ingr)
    la.append(alle)

d={a:set() for a in s_alle}  # ingredients that doesn't have a certain allegen
for a in s_alle:
    tmp=s_ingr.copy()
    for i,l in enumerate(la):
        if a not in l:
            continue
        d[a]|=tmp-li[i]
        tmp&=li[i]

no_alle=set.intersection(*d.values())

ans=0
for l in li:
    ans+=sum(i in no_alle for i in l)

print(ans)
        
            
            
