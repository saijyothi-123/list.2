# alist=[4,6,8,24,12,2]
# alist.sort(reverse=True)
# print(alist.pop(0))



l=[1,2,3,1,2,2]
i=0
b=[]
while i<len(l):
    c=l[i]
    if c not in b:
        c.append(b)
    i=i+1
print(b)
    
    