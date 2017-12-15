#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###说明：不可避免的是，python的语法与javascript非常像，所以学习python的时候，与js进行比较．

#整数 -- 与js相同
a = 100
#注意python3的print语法与python2不兼容，python2中可以print 'xxxx'，而python3必须要用括号
print(a)
a = -8080
print(a)
a = 0xff
#255
print(a)
a = 25

#格式化输出
#i am 25 years old
print('i am %d years old'%a)
a = 10
#%x--hex十六进制　%d--dec十进制　%o--oct八进制
#dec = 10,oct = 12,hex = a
print('dec = %d,oct = %o,hex = %x'%(a,a,a))

#浮点数
a = 1.23
#1.23
print(a)
a = 1.23e9
#1230000000.0
print(a)
#1230000000
print('%d'%a)

a = 0.0033333333
# %f:默认保留小数点后６位
# %e:也是保留小数点后６位
# %g:在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法
#0.003333,3.333333e-03,0.00333333
print('%f,%e,%g'%(a,a,a))
a = 0.003
#0.003000,3.000000e-03,0.003
print('%f,%e,%g'%(a,a,a))
a = 0.000033333
#0.000033,3.333300e-05,3.3333e-05
print('%f,%e,%g'%(a,a,a))
#控制精度:0.000,3.333e-05,3.33e-05
print('%.3f,%.3e,%.3g'%(a,a,a))

#字符串,单引号或者双引号，与js类似
#I'm nick
print("I'm nick")
#I'm nick
print('I\'m nick')
#I'm "nick"
print('I\'m \"nick\"')
a = 'nick'
#I am nick
print('I am %s'%a)
#多行
print('多行的时候\n可以换行输出')
#js中用``
print('''多行的时候
可以换行输出''')
# r表示不转义
# I\'m nick
print(r'I\'m nick')
# \n无效果
print(r'多行的时候\n可以换行输出')
# 注意：这里加r不影响多行，因为'''和转义是不一样的
print(r'''多行的时候
可以换行输出''')

#布尔值：True False 注意首字母大写 (js中为小写：true false)
#布尔值运算 and or not
#js中&& || !

#False
print(True and False)
#True
print(True or False)
#False
print(not True)

#空值：None (js中为null)

#变量
a = 'abc'
b = a
a = 'def'
#def
print(a)
#abc　理解引用的指向，js相同
print(b)

#常量
#Python中常量只是约定用大写表示，实际就是变量,无法保证不被修改
#js中用const定义常量，不能被修改
PI = 3.14
#3.14
print(PI)
#2
PI = 2
print(PI)

#除法/与地板除//
#/结果是浮点数，//结果是整数
a = 10 / 3
#3.3333333333333335
print(a)
a = 10 // 3
#3
print(a)
#整数的取余一定为整数
a = 10 % 3
#1
print(a)
a = 10.5 % 3
#1.5
print(a)