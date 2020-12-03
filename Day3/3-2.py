with open('3.txt','r') as f:
    mp=[line for line in f]

l=len(mp[0])-1
ans=1
slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]
for rt,dn in slopes:
    ind,trees=0,0
    for r in mp[::dn]:
        if r[ind]=='#':
            trees+=1
        ind=(ind+rt)%l
    ans*=trees
print(ans)
