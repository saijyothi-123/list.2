a=["red","maroon","yellow","olive"]
b=[]
i=0
while i<len(a):
    c=a[i]
    j=0
    d=[]
    while j<len(c):
        d.append(c[j])
        j=j+1
    b.append(d)
    i=i+1
print(b)
        
    