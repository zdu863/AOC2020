with open('input.txt','r') as f:
    data=f.read().splitlines()

ans=0
cur=set()
for line in data:
    if len(line)>0:
        for q in line:
            cur.add(q)
    else:
        ans+=len(cur)
        cur.clear()
ans+=len(cur)
print(ans)
