L = []                             #生成1*1 2*2。。。。。的结果，方法一：循环
for x in range(1,11):
    L.append(x*x)
print(L)

[x*x for x in range(1,11)]          #方法2，使用列表生成式

[x*x for x in range(1,10) if x % 2 ==0]

[m+n for m in 'ABC' for n in 'XYZ']

import os
[d for d in os.listdir('.')]      # 列出当前目录下对的所有文件和目录名

d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
    print(k, '=', v)

d = {'x':'A', 'y':'B', 'z':'C'}
[k + '=' + v for k, v in d.items()]  #列表生成式也可以使用两个变量来生成list

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]                #把一个list中所有的字符串变成小写