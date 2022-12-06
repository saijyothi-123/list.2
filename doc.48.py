# a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
# b=[]
# i=0
# while i<len(a)-2:
#     num=a[i],a[i+1],a[i+2]
#     b.append(list(num))
#     i=i+3
# print(b)






a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
b=[]
i=0
while i<len(a)-2:
    num=[a[i],a[i+1],a[i+2]]
    b.append(num)
    i=i+3
print(b)





a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
size=int(input("enter the size:"))
i=0
b=[]
while i<len(a):
    x=a[i:i+size]
    b.append(list(x))
    i=i+size
print(b)


