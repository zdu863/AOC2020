with open('input.txt','r') as f:
    data=f.read().splitlines()
data=[r.replace(' ','') for r in data]

def prnth(s):
    stack=[]
    d={}
    for i,c in enumerate(s):
        if c=='(':
            stack.append(i)
        elif c==')':
            d[stack.pop()]=i
    return d
    
def eva(s,a,b,d):
    ret=0
    i=a
    while i<=b:
        if s[i]=='(':
            val=eva(s,i+1,d[i]-1,d)
        elif s[i].isdigit():
            val=int(s[i])
            
        if i==a or s[i-1]=='+':
            ret+=val
        elif s[i-1]=='*':
            ret*=val
            
        if i in d:
            i=d[i]
        i+=1
    return ret
    
ans=0
for r in data:
    ans+=eva(r,0,len(r)-1,prnth(r))
print(ans)

    
