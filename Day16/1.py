with open('input.txt','r') as f:
    data=f.read().splitlines()

constrains=[]
for line in data[:20]:
    name,tmp=line.split(':')
    for s in tmp.split('or'):
        constrains.append([int(c) for c in s.strip().split('-')])

ans=0
for line in data[25:]:
    vals=[int(a) for a in line.split(',')]
    for v in vals:
        valid=False
        for l,h in constrains:
            if l<=v<=h:
                valid=True
                break
        if not valid:
            ans+=v
print(ans)
