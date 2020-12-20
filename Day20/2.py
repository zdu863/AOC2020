import numpy as np
from collections import Counter,defaultdict

with open('input.txt','r') as f:
    data=f.read().splitlines()

maps={}
i=0
while i<len(data):
    num=int(data[i][5:9])
    maps[num]=[]
    while True:
        i+=1
        if i==len(data) or not data[i]:
            break
        maps[num].append(data[i])
    i+=1

extra={}
d_edges={}
for num,m in maps.items():
    t,b,l,r=m[0],m[-1],''.join(r[0] for r in m),''.join(r[-1] for r in m)
    tf,bf,lf,rf=t[::-1],b[::-1],l[::-1],r[::-1]
    
    for e in [t,b,l,r,tf,bf,lf,rf]:
        if e in extra:
            extra.pop(e)
        else:
            extra[e]=num
    d_edges[num]=[t,b,l,r,tf,bf,lf,rf]

corners=[]
for k,v in Counter(extra.values()).items():
    if v==4:
        corners.append(k)
# print(corners)

# d_edges={}
# for num,m in maps.items():
#     t,b,l,r=m[0],m[-1],''.join(r[0] for r in m),''.join(r[-1] for r in m)
#     tf,bf,lf,rf=t[::-1],b[::-1],l[::-1],r[::-1]
    
# grid=[[[]for _ in range(12)]for _ in range(12)]
# m=maps[1289]  # topleft corner

# [0,90,180,270,0f,90f,180f,270f]
# rotate clockwise, flip about y axis
# matched to right side: t:90f b:90 l:0 r:0f tf:270 bf:270f lf:180f rf:180
# new right side:        b     t    r   l    bf     tf      rf      lf    

#### new bottom:            r     rf   b   bf   l      lf      t       tf

nrs=[1,0,3,2,5,4,7,6]
norient=[5,1,0,4,3,7,6,2]

cur=corners[0] # choose any of the corners as topleft corner
dupe_edges=[]
for i,e in enumerate(d_edges[cur][:4]):
    if e not in extra:
        dupe_edges.append(i)
dupe_edges=tuple(dupe_edges)

ofe={(0,2):2,(0,3):1,(1,2):3,(1,3):0}   #orientation from dupe_edges
otp=ofe[dupe_edges] # topleft corner orientation
# rso=[3,0,6,5] # right side from orientation

right=d_edges[cur][[3,0,6,5][otp]]
first_row=[(cur,otp)]
while len(first_row)<12:
    for k in d_edges:
        if k!=cur and right in d_edges[k]:
            cur=k
            ind=d_edges[k].index(right)
            orientation=norient[ind]
            right=d_edges[k][nrs[ind]]
            first_row.append((k,orientation))
            break
            
bigmap=[first_row]
# print(first_row)
    
# [0,90,180,270,0f,90f,180f,270f]
# [t,b,l,r,tf,bf,lf,rf]

# bottom from orientation: 0:b 90:rf 180:tf 270:l 0f:bf 90f:r 180f:t 270f:lf
# matched to bottom: t:0 b:180f l:90f r:270 tf:0f bf:180 lf:90 rf:270f

bfo=[1,7,4,2,5,3,0,6] #bottom from orientation
mtb=[0,6,5,3,4,2,1,7] #orientation from matched to bottom

for _ in range(11):
    last_row=bigmap[-1]
    new_row=[]
    for num,orient in last_row:
        bot=d_edges[num][bfo[orient]]   
        for k in d_edges:
            if k!=num and bot in d_edges[k]:
                ind=d_edges[k].index(bot)
                orientation=mtb[ind]
                new_row.append((k,orientation))
                break
    bigmap.append(new_row)
# print(new_row)
# print(bigmap)
def convert_to_np(mp): # also removes boundary
    tmp=[]
    for r in mp[1:-1]:
        tmp.append([int(c) for c in r[1:-1].replace('#','1').replace('.','0')])
    return np.vstack(tmp)
        
# print(convert_to_np(maps[1289]))
rows=[]
for i,r in enumerate(bigmap):
    cur=[]
    for num,orient in r:
        tmp=convert_to_np(maps[num])
        mp=np.rot90(tmp,k=orient%4,axes=(1,0))
        if orient>3:
            mp=np.flip(mp,1)
        cur.append(mp)
    rows.append(np.hstack(cur))
npmap=np.vstack(rows)

# print(npmap.shape)
# print(npmap.sum())
monster=['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']

mstr=[]
for r in monster:
    mstr.append([int(c) for c in r.replace('#','1').replace(' ','0')])
mstr=np.vstack(mstr)

# [0,90,180,270,0f,90f,180f,270f]

# print(mstr.shape)
# print(mstr.sum())

nmstr=mstr.sum()
nmap=npmap.sum()

for o in range(8):
    mp=np.rot90(mstr,k=o%4,axes=(1,0))
    if o>3:
        mp=np.flip(mp,1)
    x,y=mp.shape
    xa,ya=npmap.shape
    
    left=nmap
    found=False
    for m in range(xa-x+1):
        for n in range(ya-y+1):
            if np.multiply(mp,npmap[m:m+x,n:n+y]).sum()==nmstr:
                left-=nmstr
                found=True
    if found:
        print(left)




# ans=[]
# for k,v in Counter(edges.values()).items():
#     if v==4:
#         ans.append(k)
# print(ans)
