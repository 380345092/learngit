d = {'a':1, 'b':2, 'c':3}
for key in d :
    print(key)
for value in d.values() :
    print(value)

for ch in 'ABC' :
    print(ch)

from collections import Iterable    #判断是否为可迭代对象
#isinstance('abc', Iterable)
#isinstance([1,2,3], Iterable)
isinstance(123, Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)