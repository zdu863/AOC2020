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

print(sum(sum(r) for r in mp))
