class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

    def next3(self):
        ret=self.next
        self.next=self.next.next.next.next
        return ret
    
    def putback3(self,n3):
        n3.next.next.next=self.next
        self.next=n3

N=10**6
cups=[int(i) for i in '362981754']
cups.extend(range(10,N+1))

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
    n3=cur.next3()
        
    dest=(cur.val-2)%N+1
    while dest in {n3.val,n3.next.val,n3.next.next.val}:
        dest=(dest-2)%N+1
    
    d[dest].putback3(n3)
    cur=cur.next
    
print(d[1].next.val*d[1].next.next.val)
