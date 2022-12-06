geekcodes=[1,2,3,4]
geekcodes.append([5,6,7,8])
print(geekcodes)



check1=["learn","quiz","practise","contribute"]
check2=check1
check3=check1[:]
check2[0]="code"        
check3[1]="mcq"
count=0
for c in (check1,check2,check3):
    if c[0]=="code":
        count+=1
    if c[1]=="mcq":
        count+=10
print(count)
