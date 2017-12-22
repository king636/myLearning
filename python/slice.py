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

##　练习，利用切片，去掉字符串首尾空格(首尾可能有多个空格)
# trip()函数是可以实现去除首尾的空格，这里用自定义的方法实现
# 1，利用正则表达式实现，如下：
import re

reg = r'^(\s*)([\w\s]+?)(\s*)$'
def trim(s):
    print('s=',s)
    print('s.len=',len(s))
    if len(s) == 0:
        return ''
    gr = re.match(reg,s)
    #注意，这里有个坑：如果分组匹配完比如('','hello',' '),这时group(2)才是'hello',why?
    print(gr.groups())
    # print(gr.group(0))
    # print(gr.group(1))
    # print(gr.group(2))
    return gr.group(2)

# trim('hello')
# def trim(s):
#     if s is None or len(s) == 0:
#         return ''
#     if s[0] == ' ':
#         s = s[1:]
#     length = len(s)
#     if s[length - 1] == ' ':
#         s = s[-length:-1]
    
#     return;

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
