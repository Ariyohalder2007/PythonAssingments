def add(a, b):
    print(a + b)


def mul(a, b):
    print(a * b)


def divide(a, b):
    print(a / b)


def sub(a, b):
    print(a - b)


def cal(f, a, b):
    f(a, b)

op=input('What to Do (try: add, sub, mul, divide): ')
n1=int(input('First num: '))
n2=int(input('second num: '))
if op=='add':
    cal(add, n1, n2)
if op=='sub':
    cal(sub, n1, n2)
if op=='mul':
    cal(mul, n1, n2)
if op=='divide':
    cal(divide, n1, n2)