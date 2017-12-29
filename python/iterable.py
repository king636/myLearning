#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 本节分析迭代，列表生成式，生成器和迭代器

# 迭代
# 与js的迭代类似，js的Array Map和Set都属于迭代器，可以用for...of来遍历
# 而python的list tuple dict和set也都是可迭代对象，可以用for...in来遍历

# 判断是否可迭代，前面可变参数那有做说明：
import collections
def fn(params):
    if not isinstance(param,collections.Iterable):
        raise TypeError('is not iterable')
    pass

# 对dict的迭代
test = {
    'a':1,
    'b':'hello',
    'c':3
}    
for abc in test:
    # 依次打印a,b,c(注意a,b,c不一定按顺序，因为dict并不是按顺序保存key,只是能确认key-value是配对的)
    print(abc)
    # 依次打印对应的value
    print(test[abc])

# 可单独遍历value:
for val in test.values():
    print(val)

# key-value同时打：
for k,v in test.items():
    # key =  a , value =  1
    # key =  b , value =  hello
    # key =  c , value =  3
    print('key = ',k,', value = ',v)

## list 实现下标遍历内容
# 使用python内置的enumerate
for i,v in enumerate(['A','B','C']):
    # i =  0 , value =  A
    # i =  1 , value =  B
    # i =  2 , value =  C
    print('i = ', i, ', value = ', v)

# list中使用tuple
for x,y in [(1,1),(2,4),(3,9)]:
    print('x = ', x, ', y = ', y)


### 练习：用迭代找出list中的最小和最大值，并返回tuple
def findMinAndMax(list):
    if list is None or len(list) <= 0:
        return (None,None)
    
    print(list)
    min = list[0]
    max = list[0]
    for x in list:
        if x > max:
            max = x
        
        if x < min:
            min = x
    
    print(min,max)
    return (min,max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

### 列表生成器
# python内置非常简单却强大的生成list的生成式
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1,11)))
# 或者[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x for x in range(1,11)])

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1,11)])
# 或者[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(x * x for x in range(1,11)))

# for后面还可以加if判断:[4, 16, 36, 64, 100]
print([x * x for x in range(1,11) if x % 2 == 0])

## 使用两层循环
# ['Ax', 'Ay', 'Az', 'Bx', 'By', 'Bz', 'Cx', 'Cy', 'Cz']
print([m + n for m in ['A','B','C'] for n in ['x','y','z']])
# 只取索引匹配的：['Ax', 'By', 'Cz']
print([m + n for x,m in enumerate(['A','B','C']) for y,n in enumerate(['x','y','z']) if y == x])

##列出当前目录下的文件和目录
import os
#['basic.py', 'code.py', 'iterable.py', 'for.py', 'function.py', 'listAndTuple.py', '__pycache__', 'hello.py', 'function_my_abs.py', 'slice.py','dictAndset.py', 'regexp.py']
print([d for d in os.listdir('.')])

#dict
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    # x = A
    # y = B
    # z = C
    print(k,'=',v)

# 生成list:['x=A', 'y=B', 'z=C']
print([k + '=' + v for k,v in d.items()])

## 把list中所有字符串变小写:['afefwa', 'aaaeeddsdf']
print([s.lower() for s in ['AFefwa','AAAeedDsdf']])

# 练习：上面的实例中list元素可能是整数，那么会报错．改写让程序更健壮．
# AttributeError: 'int' object has no attribute 'lower'
# print([s.lower() for s in ['AFefwa','AAAeedDsdf',123]])

# ['afefwa', 'aaaeeddsdf']
print([s.lower() for s in ['AFefwa','AAAeedDsdf',123] if isinstance(s,str)])

####　生成器generator,列表生成式的最外层改为()即可
# 列表生成式容量有限，而用generator则可以无限：在循环的过程中推断后续元素，使用next(g)来获取

#<generator object <genexpr> at 0x7f4d4c37f468>
print((x * x for x in range(1,11)))
g = (x * x for x in range(1,11))
# 1
# next(g)每次取得下一个，一般不用
# next(g)一直执行，如果列表有限，最后会报错并StopIteration
print('next: ',next(g))
# 注意：因为前面调用了next(g),这里实际上从第二个开始
# 用循环的方式不会StopIteration
for n in g:
    print(n)

# 斐波拉契数列的函数表示
# 该函数事实上是斐波拉契数列的推演规则，与generator的定义很类似
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a + b
        n = n + 1

    return 'done'

# 1
# 1
# 2
# 3
# 5
# 8
# done
print(fib(6))

# fib函数改为generator,只需要在print(b)改写为yield b
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # 如果不需要返回值b，那么yield / yield a / yield b / yield n都可以
        # 这里返回值为b
        yield b
        a,b = b,a + b
        n = n + 1

    return 'done'

# 如何使用
o = fib(3)
# <generator object fib at 0x7f1d046b2888>
print(o)
# 1
print(next(o))
# 1
print(next(o))
# 2
print(next(o))
# StopIteration: done
# print(next(o))

# 1
# 1
# 2
# 3
# 5
# 8
for n in fib(6):
    print(n)


## 注意：用for语句时不会执行到获取返回值'done'，所以可改写如下(next超出后的报错捕获)：
g = fib(6)
# 1
# 1
# 2
# 3
# 5
# 8
# done
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break


### 练习：杨晖三角
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

def triangles(max):
    L = []
    n = 0
    while n < max:
        L.append(1)
        yield L
        


    return "done"