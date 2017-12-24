#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# slice:切片，事实上js中Array或者String的切片通过调用slice()函数．
# python的思想是一样的，但是python没有slice()函数，而是直接写：
array = [1,2,4,5]
# [1, 2] 从索引０开始取２个
print(array[0:2])
# [1, 2, 4, 5]
print(array[0:])
# [1, 2]
print(array[:2])
# 倒数切片，js不支持负数索引
# [4, 5]
print(array[-2:])
# [4] 注意倒数第一个是-1
print(array[-2:-1])
# [2, 4]
print(array[-3:-1])
# [] 因为倒数取不到1
print(array[-3:1])

## tuple用切片：
tu = (1,2,3,4)
# (2, 3)
print(tu[1:3])

# 字符串用切片，python的字符串只能用切片方式获取子串，不像js，js的字符串有substring()方法，也可以用slice()方法获取子串
str = '123456'
# 2345
print(str[1:5])
# 切片时三个数，最后一个代表间隔．如下，每隔２个取一个
# 135
print(str[::2])

##　练习，去掉字符串首尾空格(首尾可能有多个空格)
# strip()函数是可以实现去除首尾的空格
# str.strip(char),移除首尾指定的字符生成新的字符串,默认移除空格
def trim(s):
    return s.strip()

# 利用自定义函数实现：
# 1，正则表达式实现，如下：
import re

## 匹配字符串首尾可能是空格
reg = r'^(\s*)([\w\s]+?)(\s*)$'
def trim(s):
    ##　判断字符串无内容
    if len(s) == 0:
        return ''
    ## 判断字符串只包含空格（是否有更好的方式？）
    if re.match(r'^(\s*)(\s*)$', s):
        return ''
    gr = re.match(reg,s)
    #注意，这里有个坑：如果分组匹配完比如('','hello',' '),这时group(2)才是'hello',why?
    return gr.group(2)

# 2，利用切片方式实现
# 想法：从首开始，索引移动到第一个非空格；同样从尾开始，索引移动到第一个非空格．根据两次的索引来截取
def trim(s):
    if len(s) <= 0:
        return ''
    
    head = 0
    foot = -1
    while head < len(s) and s[head] == ' ':
        head = head + 1

    while foot >= -len(s) and s[foot] == ' ':
        foot = foot - 1

    return s[head:len(s) + 1 + foot]

if trim('hello ') != 'hello':
    print('测试失败!')
elif trim(' hello') != 'hello':
    print('测试失败!')
elif trim(' hello ') != 'hello':
    print('测试失败!')
elif trim(' hello  world ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim(' ') != '':
    print('测试失败!')
else:
    print('测试成功!')
