from copy import deepcopy

with open('input.txt','r') as f:
    grid=f.read().splitlines()
grid=[list(r) for r in grid]

m,n,l,o=20,20,13,13
field=[[[['.' for _ in range(m)] for _ in range(n)]for _ in range(l)]for _ in range(o)]

for i in range(8):
    field[o//2][l//2][6+i][6:14]=grid[i].copy()

def active(field,i,j,k,h):
    ret=0
    for dh in [-1,0,1]:
        for dk in [-1,0,1]:
            for di,dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
                if di==dj==dk==dh==0:
                    continue
                I,J,K,H=i+di,j+dj,k+dk,h+dh
                if 0<=I<m and 0<=J<n and 0<=K<l and 0<=H<o and field[H][K][I][J]=='#':
                    ret+=1
    return ret
    
for _ in range(6):
    field_c=deepcopy(field)
    for h,cube in enumerate(field_c):
        for k,lvl in enumerate(cube):
            for i,r in enumerate(lvl):
                for j,c in enumerate(r):
                    count=active(field_c,i,j,k,h)
                    if c=='.' and count==3:
                        field[h][k][i][j]='#'
                    elif c=='#' and (count<2 or count>3):
                        field[h][k][i][j]='.'
                
print(sum(sum(sum(r.count('#') for r in lvl) for lvl in cube)for cube in field))
