dict1={
    '1':23,
    '2':43,
    '3':1,
    '4':52
}

l=[]
for i in dict1.values():
    l.append(i)
print(max(l))
print(min(l))
