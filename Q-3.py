n=int(input("Enter the range: "))
def fibo(n):
    a, b = 0, 1

    while a < n:
        yield a
        a, b = b, a + b


a = fibo(n)
for i in a:
    print(i, end=" ")