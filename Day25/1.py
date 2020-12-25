card_pkey=14205034
door_pkey=18047856

i=0
ini=1
while True:
    i+=1
    ini*=7
    ini%=20201227
    if ini==card_pkey:
        break

ini=1
while i:
    i-=1
    ini*=door_pkey
    ini%=20201227

print(ini)
