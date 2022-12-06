
# a=["s","d","f","s","d","f","s","f","k","o","p","i","w","e","k","c"]
# b=[]
# i=1
# while i<len(a):
#     if a[i]=="f":
#         c=i
#     elif a[i]=="k":
#         d=i
#     elif a[i]=="c":
#         e=i
#     i=i+1
# print("f last appearance is",c)
# print("k last appearance is",d)
# print("c last appearance is",e)
        
        

a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
n= input("enter the character:")
k=len(a)-1-a[::-1].index(n)
print(k)