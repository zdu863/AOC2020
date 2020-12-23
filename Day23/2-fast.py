def next3(node):
    n3=d_next[node]
    d_next[node]=d_next[d_next[d_next[d_next[node]]]]
    return n3
    
def putback3(node,n3):
    d_next[d_next[d_next[n3]]]=d_next[node]
    d_next[node]=n3

N=10**6
cups=[int(i) for i in '362981754']
cups.extend(range(10,N+1))

lst=-1
d_next={}
for c in cups:
    d_next[lst]=c
    lst=c
d_next[lst]=d_next[-1]

cur=d_next[-1]
for _ in range(10**7):
    n3=next3(cur)
        
    dest=(cur-2)%N+1
    pickup={n3,d_next[n3],d_next[d_next[n3]]}
    while dest in pickup:
        dest=(dest-2)%N+1
    
    putback3(dest,n3)
    cur=d_next[cur]
    
print(d_next[1]*d_next[d_next[1]])
