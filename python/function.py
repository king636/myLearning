#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数用法
# python内置的函数
# 1. abs()取绝对值，js也有内置函数：Math.abs()
# 20
print(abs(-20))
# 参数不对，报错：TypeError: abs() takes exactly one argument (2 given)
# js不报错
# abs(-20,1)
# 参数类型不对，报错：TypeError: bad operand type for abs(): 'str'
# js的Math.abs()参数类型不对，返回NaN
# abs('a')

# 内置函数２：max,取最大值 js用Math.max()
# 8
print(max(1,8,3,5))

# 内置函数３：
# int()
# str()
# bool()

# 1
print(int('1'))
# 报错：ValueError: invalid literal for int() with base 10: 'a'
# print(int('a'))
# 1234
print(str(1234))
# None
print(str(None))
# True
print(bool(1))
# False
print(bool(None))
# False
print(bool(''))
# True
print(bool('a'))

# 内置函数：hex()
# 0xa
print(hex(10))

############################################
# 定义函数
# 函数不写return时，返回None.而js是undefined
def my_abs(x):
    if x >= 0:
        return x;
    else:
        return -x;

# 99
print(my_abs(-99))

## 函数如何在别的文件中导入？参看function_my_abs.py,使用from function import my_abs来导入
# js中我只知道只能通过宿主(比如浏览器)，在html文件中导入js文件，然后使用其函数．
# 单纯的js文件应该无法像python一样导入其他文件的函数，所以python更像c,可以导入头文件．js是脚本，寄托于宿主．

# 空函数与pass关键字，占位用，确保代码正常运行
def fun():
    pass

# pass放到判断中，代表什么也不做.如果不用pass,会有语法错误
x = 20
if x > 10:
    pass

# my_abs函数扩展，增加类型检查，以及抛出异常
# 检查参数是否是int或者float类型，如果不是，抛出TypeError异常 oprand:操作数
# js中检查x的类型：typeof x !== 'number'
# python使用raise Error对象来抛出异常，js使用throw('...')
def my_abs_extend(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#TypeError: bad operand type
# my_abs_extend('a')

### 返回多个值,事实上与js中的解构赋值类似，分析如下：
import math

# move函数根据点移动时的坐标　位移　和角度，算出新的点的坐标
# 这里参数angle=0定义了默认值，默认参数的使用：与js类似，必须写在后面
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
# 151.96152422706632 70.0
print(x,y)

# 事实上相当于以下，move函数返回的是tuple
r = move(100, 100, 60, math.pi / 6)
# (151.96152422706632, 70.0)
print(r)
# 这里的作用就是解构赋值，js中数组对应的解构赋值：[a,b] = [151.96152422706632,70.0]
(a,b) = r
# 151.96152422706632 70.0
print(a,b)


### 默认参数，可变参数，关键字参数，命名关键字参数
