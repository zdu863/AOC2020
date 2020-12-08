with open('input.txt','r') as f:
    data=f.read().splitlines()

data=[l.split() for l in data]

i,acc=0,0
visited=[0]*len(data)
while True:
    if visited[i]:
        break
    visited[i]=1
    cmd,val=data[i][0],int(data[i][1])
    if cmd=='nop': 
        i+=1
    elif cmd=='acc': 
        acc+=val
        i+=1
    else:
        i+=val
        
print(acc)
