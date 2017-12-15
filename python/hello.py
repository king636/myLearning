#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行的作用：直接运行py文件
# 1.需要赋予权限: chmod a+x hello.py
# 2.然后可直接运行: ./hello.py

# 安装python后，命令行输入python进入交互模式
# 退出输入exit()
# 这里都是在命令行不进入node交互模式，用命令python xxx.py来运行python文件
# Node.js也类似
# 基本用法

#注意一行语句结束后面不要添加空格，不然会报错：SyntaxError: invalid character in identifier
#python有严格的格式
print('hello world')
print(100 + 200 + 300)

# 多个字符串，用,隔开可以连在一起输出. ','的地方会变成空格
# 结果: hello, I'm nick ,byebye
print('hello,','I\'m nick',',byebye')

#print('please input your name:')
name = input('please input your name:\n')
print('hello,',name)

#输入的是字符串，需要转化成int,才能比较(问题：如何限制输入的是数字？)
#可以通过异常来判断，也可以使用正则表达式，分别实现如下：
#1.使用异常来判断
#定义函数
print('************** 使用异常判断输入是否是数字，有Bug用法 ******************')
def inputAndCheck():
    #代码块请使用4个空格缩进，这里回车自动缩进4个空格
    a = input('please enter number:\n')
    try:
        a = int(a)
        return int(a)
    except ValueError:
        print('输入的不是数字')
        inputAndCheck()

#输入并检查，直到输入正确为止
#注意，以下用法有问题，如果第一次就输入数字，那么a正常与０比较．如果第一次输入非数字,
#那么a将变为NoneType(理解为error时返回了未知类型,然后输入直到正常时并没有去更改a的值？)，如何修改？
a = inputAndCheck()
if a >= 0:
    print(a)
else:
    print(-a)

#上面的问题要解决，则可以把打印的语句放到函数里执行
print('************** 使用异常判断输入是否是数字，正确用法 ******************')
def inputAndCheck2():
    #代码块请使用4个空格缩进，这里回车自动缩进4个空格
    a = input('please enter number:\n')
    try:
        #支持小数
        a = float(a)
        if a >= 0:
            print(a)
        else:
            print(-a)
    except ValueError:
        print('输入的不是数字')
        inputAndCheck2()

inputAndCheck2()

#使用正则表达式来判断
print('************** 使用正则表达式判断输入是否是数字 ******************')
#使用import导入
import re
def inputAndCheck3():
    #代码块请使用4个空格缩进，这里回车自动缩进4个空格
    b = input('please enter number:\n')
    #这里的正则表达式判断浮点数，但是如果是整数就无法判断了,怎样能一起处理整数与浮点数？
    value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
    result = value.match(b)
    if result:
        b = float(b)
        if b >= 0:
            print(b)
        else:
            print(-b)
    else:
        inputAndCheck3()

inputAndCheck3()

        
