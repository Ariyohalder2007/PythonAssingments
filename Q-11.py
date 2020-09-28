t=(2, 3,1,1, 7, 2,5,3, 7, 3)
l=[]
for i in t:
    myCount=t.count(i)
    if myCount>1:
        l.append(i)
print(set(l))