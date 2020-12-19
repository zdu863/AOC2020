with open('input.txt','r') as f:
    data=f.read().splitlines()

d_len={}
def length(rule):
    if rule in d_len:
        return d_len[rule]
    next=d[rule]
    if next=='a' or next=='b':
        d_len[rule]=1
    elif type(next)==tuple:
        d_len[rule]=sum(length(n) for n in next)
    else:
        l1=sum(length(n) for n in next[0])
        l2=sum(length(n) for n in next[1])
        d_len[rule]=l1
    return d_len[rule]

def parts(s,rules):
    ret,i=True,0
    for n in rules:
        l=length(n)
        ret&=match(s[i:i+l],n)
        i+=l
    return ret and i==len(s)
    
def match(s,rule):
    next=d[rule]
    if next=='a' or next=='b':
        return s==next
    if type(next)==tuple:
        return parts(s,next)
    return parts(s,next[0]) or parts(s,next[1])

d={}
for row,l in enumerate(data):
    if not l:
        break
    k,v = l.split(':')
    if 'a' in v:
        val='a'
    elif 'b' in v:
        val='b'
    elif '|' in v:
        val=[tuple(i.split()) for i in v.split('|')]
    else:
        val=tuple(v.split())
    d[k]=val

ans=0
begin=False
for l in data[row+1:]:
    if len(l)%8!=0:
        continue
    nparts=len(l)//8
    for i in range(1,nparts//2+nparts%2):
        rules=tuple(['42']*(nparts-i)+['31']*i)
        if parts(l,rules):
            ans+=1
            break
print(ans)
