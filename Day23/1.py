class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def next3(node):
    tmp=node.next
    node.next=node.next.next.next.next
    tmp.next.next.next=None
    return tmp
    
def find(head,val):
    while head.val!=val:
        head=head.next
    return head

def print_ring(head):
    i=0
    ret=[]
    node=head
    while i<9:
        ret.append(node.val)
        node=node.next
        i+=1
    print(ret)
    
cups=[int(i) for i in '362981754']

head=Node(cups[0])
node=head
for c in cups[1:]:
    node.next=Node(c)
    node=node.next
node.next=head

cur=head
i=0
while i<100:
    n3=next3(cur)
    clabel=cur.val
    
    dest=clabel-1 if clabel!=1 else 9
    while dest in {n3.val,n3.next.val,n3.next.next.val}:
        dest=dest-1 if dest!=1 else 9
        
    dnode=find(cur,dest)
    tmp=dnode.next
    dnode.next=n3
    n3.next.next.next=tmp
    cur=cur.next
    i+=1
print_ring(cur)
