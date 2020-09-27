l=[]
n3=int(input('Enter Length of list: '))
l2=[]
for i in range(0, n3):
    n2=input('Enter list element: ')
    l.append(n2)
n=int(input('Enter n: '))
for i in l:
    if len(i)>n:
        l2.append(i)
print(l2)
