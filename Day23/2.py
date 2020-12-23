class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def next3(node):
    ret=node.next
    node.next=node.next.next.next.next
    return ret
    
def putback3(dnode,n3):
    n3.next.next.next=dnode.next
    dnode.next=n3

N=10**6
cups=[int(i) for i in '362981754']
cups.extend(list(range(10,N+1)))

d={}
dummy=Node(-1)
node=dummy
for c in cups:
    node.next=Node(c)
    node=node.next
    d[c]=node
node.next=dummy.next

cur=dummy.next
for _ in range(10**7):
    n3=next3(cur)
        
    dest=(cur.val-2)%N+1
    while dest in {n3.val,n3.next.val,n3.next.next.val}:
        dest=(dest-2)%N+1
    
    putback3(d[dest],n3)
    cur=cur.next
    
print(d[1].next.val*d[1].next.next.val)
