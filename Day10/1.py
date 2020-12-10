
with open('input.txt','r') as f:
    data=f.read().splitlines()

data=[int(i) for i in data]

data.sort()
data.append(data[-1]+3)

d1,d3=0,0
lst=0
for j in data:
    d1+=(j-lst)==1
    d3+=(j-lst)==3
    lst=j
print(d1*d3)
