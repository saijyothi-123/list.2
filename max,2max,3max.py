# list=[10,15,20,24,30,40]
# max=list[0]
# sec_max=list[0]
# third_max=list[0]
# i=0
# while i<len(list):
#     if list[i]>max:
#         max=list[i]
#     i=i+1
# i=0
# while i<len(list):
#     if list[i]>sec_max and list[i]!=max:
#         sec_max=list[i]
#     i=i+1
# i=0
# while i<len(list):
#     if list[i]>third_max and list[i]!=max and list[i]!=sec_max:
#         third_max=list[i]
#     i=i+1
# print(max)
# print(sec_max)
# print(third_max)



a=[[1,2,3,],[2,4,4],[1,2]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    b.append(sum)
    i=i+1
print(b)