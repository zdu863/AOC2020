with open('input.txt','r') as f:
    d1,d2=f.read().split('\n\n')

p1=[int(i) for i in d1.splitlines()[1:]]
p2=[int(i) for i in d2.splitlines()[1:]]

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
