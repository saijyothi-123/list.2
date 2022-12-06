
# INSERT "20"in every given list after every 4th element
a=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
i=1
n=4
while i<=4:
    a.insert(n,20)
    n=n+5
    i=i+1
print(a)
 
 
 # INSERT "Z"after every 3rd element in a given list
a=["s","d","f","j","s","a","j","d","f","d"]
i=1
n=3
while i<=3:
    a.insert(n,"Z")
    n=n+4
    i=i+1
print(a)



# insert 20 the num which is divisible by 4:
# a=[1,3,5,7,9,11,0,2,4,6,8,9,4,3,0]
# i=1
# while i<len(a):
#     if (i+1)%4==0:
#         a.insert(i+1,20)
#     i=i+1
# print(a)