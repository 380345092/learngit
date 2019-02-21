L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack,']
print(L[0:3])    #索引到3为止，但是不包括3
print(L[:2])
print(L[-2:])
print(L[-2:-1])   #倒数第一个元素的索引是-1，不是0

L = list(range(100))
print(L[0:10])          #前10个数
print(L[-10:-1])        #后10个数
print(L[10:20])         #前11-20个数
print(L[0:10:2])        #前10个数，每2个取1个
print(L[::5])           #所有数，每5个取1个
print(L[::])


range(5)[:3]

'abcdefg'[:3]

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')