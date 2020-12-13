with open('input.txt','r') as f:
    data=f.read().splitlines()

depart=int(data[0])
bus=[int(d) for d in data[1].split(',') if d!='x']

w=depart
for b in bus:
    wait=(-depart)%b
    if wait<w:
        w=wait
        ind=b
        
print(ind*w)
