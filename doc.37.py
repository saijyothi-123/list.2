#pair up the consecutive elemnts of given list
# 
a=[1,2,3,4,5,6]
b=[]
i=0
while i<len(a)-1:
    num=a[i],a[i+1]
    b.append(list(num))
    i=i+1
print(b)

# pair of adjacent numbers
a=[1,2,3,4,5]
b=[]
i=0
while i<len(a)-1:
    num=a[i],a[i+1]
    b.append(list(num))
    i=i+1
print(b)



