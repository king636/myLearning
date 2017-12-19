#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for...in循环的用法
a = ['Michael','Bob','Nick']
for name in a:
    # Michael
    # Bob
    # Nick
    print(name)

## 注意：js中for(key in array),只有数组支持用for in，取到的是索引．
## js中数组或者Map或者Set用for of时，取到的是索引对应的值，与python这里相同

# range()函数生成整数序列
# range(0, 5)
print(range(5))
# 使用list()将序列转换为list, [0, 1, 2, 3, 4]
print(list(range(5)))

# 一次打印0-9, range()用在for...in中自动转换为list
for value in range(10):
    print(value)