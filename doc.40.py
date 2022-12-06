a=[[1,2,4],[2,4,4],[1,2]]
b=[]
i=0
while i<len(a):
    sum=0
    j=0
    while j<len(a[i]):
        sum=sum+a[j][i]
        j=j+1
    b.append(sum)
    i=i+1
print(b)




a1=[[1],[2,4,4],[1,2],[4]]
a=[[1,"",""],
   [2,4,4],
   [1,2,""],
   [4,"",""]]

x=[]
i=0
while i<len(a):
    j=0
    sum=0
    while j<len(a):
        b=a[j][i]
        if type (b)==int:
            sum+=b
        j=j+1
    x.append(sum)
    i=i+1
print(x)
    
