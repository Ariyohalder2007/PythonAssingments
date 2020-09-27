d={'a':5,'b':94,'c':89,'z':46,'e':12}
f=list(d.values())
a=f[0]
b=f[0]
c=f[0]
for i in f:
    if i>a :
        a=i
for i in f:
    if i>b :
        if i>=a:
            print('',end='')
        else:
            b=i
for i in f:
    if i>c :
        if i<a and i<b:
            c=i
        
        
print('the first largest value in the dictionary','is ',a)
print('the second largest value in the dictionary','is ',b)
print('the third largest value in the dictionary','is ',c)