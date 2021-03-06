with open('input.txt','r') as f:
    data=f.read().splitlines()
data=[list(r.replace(' ','')) for r in data]

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
    i=a
    while i<=b:
        if s[i]=='(':
            j=d[i]
            s[i]=str(eva(s,i+1,j-1,d))
            while i<j:
                i+=1
                s[i]=None
        i+=1
        
    cur,ret=0,1
    for c in s[a:b+1]:
        if c==None:
            continue
        if c.isdigit():
            cur+=int(c)
        elif c=='*':
            ret*=cur
            cur=0
    ret*=cur
    return ret

ans=0
for r in data:
    ans+=eva(r,0,len(r)-1,prnth(r))
print(ans)

    
