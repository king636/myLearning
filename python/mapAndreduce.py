#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### 高阶函数，python这里与js几乎一样的．函数的参数可以接收函数，函数也可以返回函数．
def add(x,y,f):
    return f(x) + f(y)

# 5
print(add(2,3,abs))


### 与js一样，高阶函数有:map/reduce,filter,sort
## map把函数作用在一个iterable上并返回一个iterator(map对象).而js中map把函数作用在Array的每一个元素并把结果生成一个新的Array．
def f(x):
    return x * x

r = map(f,(x for x in range(10)))
# <map object at 0x7f65f535f7b8>
print(r)
# list(),将序列转化为list: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(r))

## reduce也是把函数作用在序列上，但是函数必须带两个参数，把结果继续和序列下一个元素做累积计算, 注意计算的结果返回
# reduce不能直接用，需要导入
from functools import reduce
def f(x,y):
    return x + y

r = reduce(f,(x for x in range(10)))
# 45
print(r)

## 实例：字符串转换为int
from functools import reduce

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def char2num(s):
    return DIGITS[s]

def str2num(s):
    return reduce(lambda x,y: x * 10 + y, map(char2num,s))

# 123
print(str2num('123'))

## lambda的用法，这里等价于
def fn(x,y):
    return x * 10 + y

### 练习一：利用map()，将用户输入的不规范英文名字，变为首字母大写其他字母小写．
def normalize(name):
    return name[0].upper() + name[1:].lower();

L1 = ['aNiCK','aafw','QFEFWF']
L2 = list(map(normalize,L1))
# ['Anick', 'Aafw', 'Qfefwf']
print(L2)

### 用lambda改写,如果需要对输入进行判错，以及方法复用，用lambad并不合适．
L2 = list(map(lambda name: name[0].upper() + name[1:].lower(),L1))
# ['Anick', 'Aafw', 'Qfefwf']
print(L2)

###　对输入进入判错
def normalize(name):
    if name is None:
        print("input can't be none")
    return name[0].upper() + name[1:].lower();

L1 = None
# 这里用map会报错：TypeError: 'NoneType' object is not iterable
# 所以并不需要对输入进行判断是否为None,而且在使用map前判断
# L2 = list(map(normalize,L1))
# print(L2)

if L1 == None:
    # input can't be none
    print("input can't be none")

L1 = []
L2 = list(map(normalize,L1))
# []
print(L2)

