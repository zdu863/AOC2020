arr=[7,12,1,0,16,2]

d={a:[i] for i,a in enumerate(arr)}

lst=arr[-1]
for i in range(len(arr),2020):
    if len(d[lst])==1:
        spoken=0
    else:
        spoken=d[lst][-1]-d[lst][-2]
    if spoken in d:
        d[spoken].append(i)
    else:
        d[spoken]=[i]
    lst=spoken
print(spoken)
