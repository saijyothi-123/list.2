1# writw a python programm to join adjacent members of given list:


a=["1","2","3","4","5","6","7","8"]
i=0
b=[]
while i<len(a)-1:
    num=a[i]+a[i+1]
    b.append(num)
    i+=2
print(b)



a=["1","2","3"]
i=0
b=[]
while i<len(a)-1:
    num=a[i]+a[i+1]
    b.append(num)
    i=i+2
print(b)