with open('input.txt','r') as f:
    data=f.read().splitlines()

N=501
mp=[[0 for _ in range(N)] for _ in range(N)]
cx,cy=N//2,N//2

d={'e':(0,2),'se':(1,1),'sw':(1,-1),'w':(0,-2),'nw':(-1,-1),'ne':(-1,1)}

for line in data:
    i,l=0,len(line)
    x,y=cx,cy
    while i<l:
        if line[i] in d:
            dx,dy=d[line[i]]
            i+=1
        else:
            dx,dy=d[line[i:i+2]]
            i+=2
        x+=dx
        y+=dy
    if mp[x][y]==0:
        mp[x][y]=1
    else:
        mp[x][y]=0

def neighbors(mp,x,y):
    ret=0
    for dx,dy in d.values():
        X,Y=x+dx,y+dy
        if 0<=X<N and 0<=Y<N and mp[X][Y]==1:
            ret+=1
    return ret

days=0
while days<100:
    mp_c=[r.copy() for r in mp]
    for i,r in enumerate(mp_c):
        for j,c in enumerate(r):
            if (i-j)%2==1:
                continue
            count=neighbors(mp_c,i,j)
            if c==1 and (count==0 or count>2):
                mp[i][j]=0
            elif c==0 and count==2:
                mp[i][j]=1
    days+=1
                
print(sum(sum(r) for r in mp))

    
