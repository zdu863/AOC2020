import re
with open('2.txt','r') as f:
    count=0
    for line in f:
        i1,i2,ch,_,s,_=re.split('\W',line)
        count+=((s[int(i1)-1]==ch)+(s[int(i2)-1]==ch)==1)
    print(count)
