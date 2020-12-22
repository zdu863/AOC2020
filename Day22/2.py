with open('input.txt','r') as f:
    d1,d2=f.read().split('\n\n')

p1=[int(i) for i in d1.splitlines()[1:]]
p2=[int(i) for i in d2.splitlines()[1:]]

def play(p1,p2):
    s1,s2=set(),set()
    while p1 and p2:
        if p1 in s1 or p2 in s2:
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
