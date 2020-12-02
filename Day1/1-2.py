arr=[]
d={}
with open('1.txt','r') as f:
    for line in f:
        a=int(line)
        if 2020-a in d:
            b=d[2020-a]
            print(a*b*(2020-a-b))
            break
        for i in arr:
            d[a+i]=a
        arr.append(a)
