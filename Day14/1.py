with open('input.txt','r') as f:
    data=f.read().splitlines()

mem={}
for line in data:
    l=line.split()
    if l[0]=='mask':
        msk=l[2]
    else:
        ind,val=int(l[0][4:-1]),int(l[2])
        val=format(val,'036b')
        result=[]
        for i,m in enumerate(msk):
            if m!='X':
                result.append(m)
            else:
                result.append(val[i])
        mem[ind]=int(''.join(result),2)
print(sum(mem.values()))
