with open('input.txt','r') as f:
    data=f.read().splitlines()

data=[l.split() for l in data]
n=len(data)

def run(data):
    i,acc=0,0
    visited=[0]*n
    while True:
        if i==n:
            end=True
            break
        if i>n or visited[i]:
            end=False
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
        
    return end,acc
        
for i in range(n):
    if data[i][0]=='nop':
        data[i][0]='jmp'
        end,acc=run(data)
        if end:
            print(acc)
            break
        data[i][0]='nop'
    elif data[i][0]=='jmp':
        data[i][0]='nop'
        end,acc=run(data)
        if end:
            print(acc)
            break
        data[i][0]='jmp'
