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

def play(p1,p2):
    s1,s2=set(),set()
    while p1 and p2:
        if p1 in s1 and p2 in s2:
            return True,p1
        s1.add(p1)
        s2.add(p2)
        p1,p2=list(p1),list(p2)
        c1,c2=p1.pop(0),p2.pop(0)
        if len(p1)>=c1 and len(p2)>=c2:
            w1,_=play(tuple(p1[:c1]),tuple(p2[:c2]))
        else:
            w1=(c1>c2)
        if w1:
            p1.extend([c1,c2])
        else:
            p2.extend([c2,c1])
        p1,p2=tuple(p1),tuple(p2)
    if p1:
        return True,p1
    return False,p2

w,p=play(tuple(p1),tuple(p2))
ans=0
for i in range(len(p)):
    ans+=(i+1)*p[-(i+1)]
print(ans)
