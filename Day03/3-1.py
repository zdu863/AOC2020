with open('3.txt','r') as f:
    mp=[line for line in f]

l=len(mp[0])-1
ind,trees=0,0
for r in mp:
    if r[ind]=='#':
        trees+=1
    ind=(ind+3)%l
print(trees)
