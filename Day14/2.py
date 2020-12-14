with open('input.txt','r') as f:
    data=f.read().splitlines()

mem={}
for line in data:
    l=line.split()
    if l[0]=='mask':
        msk=l[2]
    else:
        ind,val=int(l[0][4:-1]),int(l[2])
        ind=format(ind,'036b')
        result=[]
        for i,m in enumerate(msk):
            if m=='0':
                result.append(ind[i])
            else:
                result.append(m)
                
        possible=[]
        idx=[i for i,r in enumerate(result) if r=='X']
        nx=len(idx)
        for n in range(2**nx):
            tmp=result.copy()
            for i,v in enumerate(format(n,f'0{nx}b')):
                tmp[idx[i]]=v
            possible.append(''.join(tmp))
        for p in possible:
            mem[int(p,2)]=val
print(sum(mem.values()))
