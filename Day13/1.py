with open('input.txt','r') as f:
    data=f.read().splitlines()

depart=int(data[0])
bus=[int(d) for d in data[1].split(',') if d!='x']

w=depart
for b in bus:
    wait=(b-depart%b)%b
    if wait<w:
        w=wait
        id=b
        
print(id*w)
