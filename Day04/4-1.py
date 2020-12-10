import re
with open('input.txt','r') as f:
    data=f.read().splitlines()
data.append(['']) # add an empty line (or the last passport won't be processed)

fields={'byr','iyr','eyr','hgt','hcl','ecl','pid'}

cur=set()
cnt=0
for r in data:
    if len(r)>1:
        for it in re.split('[ :]',r)[::2]:
            cur.add(it)
    else:
        if fields.issubset(cur):
            cnt+=1
        cur.clear()
print(cnt)
