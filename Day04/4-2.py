import re
def check(f,s):
    if f=='byr':
        return len(s)==4 and 1920<=int(s)<=2002
        
    if f=='iyr':
        return len(s)==4 and 2010<=int(s)<=2020
        
    if f=='eyr':
        return len(s)==4 and 2020<=int(s)<=2030

    if f=='hgt':
        unit,val=s[-2:],s[:-2]
        return val.isdigit() and ((unit=='cm' and 150<=int(val)<=193) or (unit=='in' and 59<=int(val)<=76))
        
    if f=='hcl':
        hair=set('0123456789abcdef')
        return len(s)==7 and s[0]=='#' and set(s[1:]).issubset(hair)

    if f=='ecl':
        return s in {'amb','blu','brn','gry','grn','hzl','oth'}
        
    if f=='pid':
        return len(s)==9 and s.isdigit()

with open('input.txt','r') as f:
    data=f.read().splitlines()
data.append(['']) # add an empty line (or the last passport won't be processed)

fields={'byr','iyr','eyr','hgt','hcl','ecl','pid'}

cur={}
cnt=0
for r in data:
    if len(r)>1:
        l=re.split('[ :\n]',r)
        for k,v in zip(l[::2],l[1::2]):
            cur[k]=v
    else:
        valid=True
        for f in fields:
            if not (f in cur and check(f,cur[f])):
                valid=False
                break
        cnt+=valid
        cur.clear()
print(cnt)
