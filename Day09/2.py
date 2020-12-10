with open('input.txt','r') as f:
    data=f.read().splitlines()

data=[int(i) for i in data]

p_sum=0
p={0:0}
target=1038347917
for i,d in enumerate(data,1):
    p_sum+=d
    if p_sum-target in p:
        ind=p[p_sum-target]
        break
    p[p_sum]=i
    
arr=data[ind:i]
print(min(arr)+max(arr))
