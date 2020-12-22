with open('input.txt','r') as f:
    data=f.read().splitlines()

p1,p2=[],[]
f1=True
for line in data:
    if not line or line=='Player 1:':
        continue
    if line=='Player 2:':
        f1=False
        continue
    if f1:
        p1.append(int(line))
    else:
        p2.append(int(line))

while p1 and p2:
    c1,c2=p1.pop(0),p2.pop(0)
    if c1>c2:
        p1.extend([c1,c2])
    else:
        p2.extend([c2,c1])
p=p1 or p2

ans=0
for i in range(len(p)):
    ans+=(i+1)*p[-(i+1)]
print(ans)
