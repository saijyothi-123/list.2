a=["https://wwww.w3resource.net"]
b=[".com",".edu",".tv","https",".net"]
for i in a:
    for j in b:
        print(j)
        if j in i:
            print(True)
        else:
            print(False)