from math import cos,sin,radians
with open('input.txt','r') as f:
    data=f.read().splitlines()

x,y=0,0
u,v=1,0

drc={'N':(0,1),'S':(0,-1),'W':(-1,0),'E':(1,0)}

for c in data:
    d,val=c[0],int(c[1:])
    if d in drc:
        dx,dy=drc[d]
        x+=val*dx
        y+=val*dy
    elif d in {'L','R'}:
        t=radians(val)
        ct,st=cos(t),sin(t)
        if d=='L':
            u,v=u*ct-v*st,u*st+v*ct
        else:
            u,v=u*ct+v*st,u*(-st)+v*ct
    else:
        x+=u*val
        y+=v*val

print(abs(x)+abs(y))
