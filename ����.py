counter = 100  #赋值整形变量
miles = 1000.0 # 浮点型
name = 'john'  #字符串

print(counter)
print(miles)
print(name)

a = b = c = 1
print (a)

a, b, c, =1, 2, 'jhon'
print(a), print(b), print(c)

a = 'runoob'
a[-1:]

str = 'Hello World!'
print(str)
print(str[0])
print(str[2:7])
print(str[2:])
print(str * 2)
print(str + 'TEST')

L = list(range(10))
L[::2]   # 取偶数

list= ['runoob', 786, 2.23, 'john', 70.2]     #列表 List
tinylist = [123, 'john']
 print(list)
 print(list[0])
 print(list[1:3])
 print(list[2:])
 print(tinylist * 2)
 print(list + tinylist)

 dict = {}                 # 字典
 dict['one'] = 'This is one'
 dict[2] = 'This is two'

 tinydict = {'name': 'john', 'code': '6734', 'dept': 'sales'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())