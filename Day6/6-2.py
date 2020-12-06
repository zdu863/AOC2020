with open('input.txt','r') as f:
    data=f.read().splitlines()

ans=0
cur=set('abcdefghijklmnopqrstuvwxyz')
for line in data:
    if line:
        cur&=set(line)
    else:
        ans+=len(cur)
        cur=set('abcdefghijklmnopqrstuvwxyz')
ans+=len(cur)
print(ans)
