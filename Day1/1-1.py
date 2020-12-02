d=set()
with open('1.txt','r') as f:
    for line in f:
        a=int(line)
        if 2020-a in d:
            print(a*(2020-a))
            break
        d.add(a)
