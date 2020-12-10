with open('input.txt','r') as f:
    data=f.read().splitlines()    

ids=[]
for seat in data:
    r,c=seat[:7],seat[-3:]
    r=r.replace('F','0').replace('B','1')
    c=c.replace('L','0').replace('R','1')
    ids.append(8*int(r,2)+int(c,2))

ids.sort()
cur=ids[0]
for i in ids[1:]:
    if i!=cur+1:
        print(cur+1)
        break
    cur=i
