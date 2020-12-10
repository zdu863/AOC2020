from bisect import bisect_left

with open('input.txt','r') as f:
    data=f.read().splitlines()

data=[int(i) for i in data]

data.sort()
data.append(data[-1]+3)

n=len(data)
dp=[0]*n
for i in range(n):
    if data[i]<=3:
        dp[i]=2**i
        continue
    ind=bisect_left(data,data[i]-3)
    dp[i]=sum(dp[ind:i])
    
print(dp[-1])
    
    
