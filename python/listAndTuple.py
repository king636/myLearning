#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python内置的list数据类型，与js的Array类似
# 写法与js相同
list = [1,2,3,'hello']
# [1, 2, 3, 'hello']
print(list)
# js中用.length获取长度
# 4
print(len(list))
# js同样用索引访问元素
# 3
print(list[2])
# python越界访问会报错：IndexError: list index out of range
# 而js是返回undefined
# print(list[4])

# python索引为负数时，倒数依次返回元素，而js不支持该用法，会返回undefined
# 返回最后一个，hello
print(list[-1])

# js中索引越界赋值，会动态改变数组长度．python不支持,报错：IndexError: list assignment index out of range
# list[4] = 10

# 插入元素到末尾，用append()函数. js的数组用push()函数
list.append(10)
# [1, 2, 3, 'hello', 10]
print(list)

# 删除末尾的元素用pop()，与js一样
list.pop()
# [1, 2, 3, 'hello']
print(list)

# 插入元素到指定位置,insert()函数, js用splice()来操作
# [1, 'hahaha', 2, 3, 'hello']
list.insert(1,'hahaha')
print(list)

# 删除指定位置用pop(i),而js不支持该用法，js中pop()不管参数，只会删除末尾元素．js用splice()来删除与替换指定位置元素
list.pop(1)
# [1, 3, 'hello']
print(list)

# 多维数组，与js一样
list = [1,2,['abc',3]]
# abc
print(list[2][0])

### Tuple,与list类似，但是初始化后不可修改
tuple = (1,2,3,'ABC')
# (1, 2, 3, 'ABC')
print(tuple)
# ABC
print(tuple[len(tuple) - 1])
# 不支持修改，报错：TypeError: 'tuple' object does not support item assignment
# tuple[0] = 'a'
# 也不支持append(),insert()等方法

# tuple不可变，在要求不可变时，尽量用tuple不用list
# 定义空的tuple
t = ()
# ()
print(t)

# 注意：定义一个元素的tuple时，需要加逗号，否则会被当成整数
t = (2)
# 2
print(t)
t = (2,)
# (2,)
print(t)
# 2
print(t[0])
