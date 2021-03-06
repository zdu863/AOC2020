with open('input.txt','r') as f:
    data=f.read().splitlines()

bus,a=[],[]
for i,d in enumerate(data[1].split(',')):
    if d=='x':
        continue
    b=int(d)
    bus.append(b)    
    a.append(-i)

def bezout(a,b):
    if a%b==0:
        return 0,1
    q,r=a//b,a%b
    m,n=bezout(b,r)
    return n,m-n*q

prod=1
for b in bus:
    prod*=b

ans=0
for i,b in enumerate(bus):
    m,n=bezout(prod//b,b)
    ans+=a[i]*m*prod//b

print(ans%prod)
