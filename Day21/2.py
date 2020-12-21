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
        
d1={}  # ingredients that have a certain allegen
for a in s_alle:
    tmp=s_ingr.copy()
    for i,l in enumerate(la):
        if a not in l:
            continue
        tmp&=li[i]
    d1[a]=list(tmp)

determined=set()
while len(determined)<len(d1):
    for k,l in list(d1.items()):
        if len(l)==1:
            v=l[0]
            determined.add(v)
            for k1 in d1:
                if k1!=k and v in d1[k1]:
                    d1[k1].remove(v)

print(','.join([v[0] for k,v in sorted(d1.items(),key=lambda x:x[0])]))
