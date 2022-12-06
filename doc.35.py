l = [1234, 122, 1984, 19372, 100]
result = True 
d = str(l[0])
print(d)
for i in l:
    c = str(i)
    if d[0] != c[0]:
        result = False
        break
    else:
        continue
print(result)

