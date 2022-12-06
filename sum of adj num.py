# sum of adjacent num

a=[1,2,3,4,5,6]
b=[]
i=0
while i<len(a)-1:
    num=a[i]+a[i+1]
    b.append(num)
    i=i+1
print(b)


