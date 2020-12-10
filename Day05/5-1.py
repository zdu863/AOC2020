with open('input.txt','r') as f:
    data=f.read().splitlines()
    
max_id=0
for seat in data:
    r,c=seat[:7],seat[-3:]
    r=r.replace('F','0').replace('B','1')
    c=c.replace('L','0').replace('R','1')
    max_id=max(max_id,8*int(r,2)+int(c,2))
print(max_id)
