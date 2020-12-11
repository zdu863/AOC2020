with open('input.txt','r') as f:
    grid=f.read().splitlines()
grid=[list(r) for r in grid]

m,n=len(grid),len(grid[0])

def occupied(grid,i,j):
    ret=0
    m,n=len(grid),len(grid[0])
    for di,dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        I,J=i+di,j+dj
        while 0<=I<m and 0<=J<n:
            if grid[I][J]=='#':
                ret+=1
                break
            elif grid[I][J]=='L':
                break
            I+=di
            J+=dj
    return ret

while True:
    stable=True
    grid_c=[r.copy() for r in grid]
    for i,r in enumerate(grid_c):
        for j,c in enumerate(r):
            count=occupied(grid_c,i,j)
            if c=='L' and count==0:
                grid[i][j]='#'
            elif c=='#' and count>=5:
                grid[i][j]='L'
            stable&=(r[j]==grid[i][j])
    if stable:
        break
        
ans=0
for i in range(m):
    for j in range(n):
        if grid[i][j]=='#':
            ans+=1
print(ans)
    
        
    
