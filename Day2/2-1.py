import re
with open('2.txt','r') as f:
    count=0
    for line in f:
        v_min,v_max,ch,_,s,_=re.split('\W',line)
        count+=(int(v_min)<=s.count(ch)<=int(v_max))
    print(count)
