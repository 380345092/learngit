
#list和生成器generator的用法区别把[]换成()

L = [x*x for x in range(10)]
print(L)

g = (x*x for x in range(10))
print(g)
next(g)


g=(x*x for x in range(10))
for n in g:
    print(n)


#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max :
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max :
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
for n in fib(6):
    print(n)
    # 直接用for 拿不到return的值
g = fib(6)
while True :
    try :
        x = =next(g)
        print('g', x)
    except StopIteration as e :
        print('Generator return value :', e.value)
        break



def odd() :
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)

#杨辉三角
L = [1]
while True:
    yield L
    L = [1] + [L[i - 1] + num for i, num in enumerate(L) if i] + [1]