def Factorial(n):
    factor=1
    if n>0:
        for i in range(1, n+1):
            factor=factor*i
        print(factor)

    

n=int(input('Enter: '))
Factorial(n)
