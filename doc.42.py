l=["a","b","c","d","e","f","g","h"]
b=[]
i=0
c=[]
while i<len(l):
    d=l[i]
    if d>l[2]:
        b.append(d)
    else:
        c.append(d)
    i=i+1
    k=b+c
print(k)