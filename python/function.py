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
# 与js一样(不过js是用[]),解构赋值的层级也需要对应
(a,b,(c,d)) = (1,2,(3,4))
# c = 3
print('c = ' + str(c))
# 当然也可以和js一样，python的list也可以解构赋值(tuple和list基本是一样的，除了不可变性质)
[a,b,[c,d]] = [10,20,[30,40]]
print('c = ' + str(c))

# js可以从对象中解构赋值，python是否可以从dict解构赋值呢？
# 报错：SyntaxError: can't assign to literal
# {a,b} = {
#     'name':'nick',
#     'age':30,
# }

# 根据上面报错的提示，不能赋值给literal, 修改为tuple
(a,b) = {
    'name':'nick',
    'age':30,
}
# 赋值的是key：name: name,age: age
print('name: ' + a + ',age: ' + b)
# 不像js,python的dict只能解构到key,要获取value,如下:
person = {
    'name':'nick',
    'age':30,
}

(a,b) = person
# name: nick
print('name: ' + person[a])
# 等价于
# name: nick
print('name: ' + person['name'])

# 加入层次和使用list
person = {
    'name':'nick',
    'age':30,
    'address':{
        'city':'Xiamen',
        'country':'China'
    }
}
# 报错：ValueError: too many values to unpack (expected 2)
# 所以dict的解构不能使用层次，那么就需要二次解构了
# (a,b,(c,d)) = person


(a,b,c) = person
# address
print(c)
(a,b) = person[c]
# city
# 这里经过二次解构
print(a)

### 上面的tuple换成list也是一样的，说明list和tuple在解构赋值时是一样用法
[a,b,c] = person
# address
print(c)
[a,b] = person[c]
# city
print(a)

### 默认参数，可变参数，关键字参数，命名关键字参数
## 注意默认参数可能会发生改变的情况
def abc(L = []):
    L.append('END')
    return L

# 第一次调用默认参数:['END']
print(abc())
# 第二次调用:['END', 'END']
# L每次调用后被改变，因为函数定义的时候python就算出默认参数变量L的值．
# js也有类似的问题，所以默认参数一定要指向不可变对象
print(abc())

# 默认参数的问题可以修改如下：
def xyz(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

# ['END']
print(xyz())
# ['END']
print(xyz())

## 可变参数
#　定义一个函数，参数可传入list或者tuple
# 通过导入collections模块，判断参数是否是Iterable(list或tuple), 如果是才能使用for...in
import collections
def calc(numbers):
    if not isinstance(numbers,collections.Iterable):
        raise TypeError('is not iterable')
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum 
# 用法：
# 14
print(calc([1,2,3]))
# 14
print(calc((1,2,3)))
# TypeError: is not iterable
# print(calc(1))

#　改为可变参数，加*
def calc(*numbers):
    if not isinstance(numbers,collections.Iterable):
        raise TypeError('is not iterable')
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum 

# 14
print(calc(1,2,3))
# 不能再传入list了，报错：TypeError: can't multiply sequence by non-int of type 'list'
# print(calc([1,2,3]))
# 这时要改为：
li = [1,2,3]
# 14
print(calc(li[0],li[1],li[2]))
# 再改：*list 表示把list的所有元素作为可变参数传入
# 14
print(calc(*li))
# 0
print(calc())

## 关键字参数　**
# 关键字参数组装成dict，参数个数任意
def registe(name,age,**other):
    print('name:',name,',age:',',other:',other)

# name: nick ,age: ,other: {}
registe('nick',30)
# name: nick ,age: ,other: {'city': 'Xiamen', 'country': 'China'}
registe('nick',30,city='Xiamen',country='China')
# 关键字参数用处：比如注册时，输入必须信息后，还可以输入额外信息
# 与可变参数类型:
extra = {
    'city':'Xiamen',
    'country':'China'
}
# name: Bob ,age: ,other: {'city': 'Xiamen', 'country': 'China'}
registe('Bob',50,city=extra['city'],contry=extra['country'])
# 简化用法
# name: Bob ,age: ,other: {'city': 'Xiamen', 'country': 'China'}
registe('Bob',50,**extra)

## 命名关键字参数
# 对于关键字参数，如果要限制参数名字，使用命名关键字参数，用＊隔开
def registe(name,age,*,city,country):
    print(name,age,city,country)
# TypeError: registe() missing 2 required keyword-only arguments: 'city' and 'country'
# 可见，命名关键字参数个数一致,且参数名要写，还要写对
# registe('Nick',30)
# nick 20 Shanghai China
registe('nick',20,city='Shanghai',country='China')
# 如果用可变参数，那么就不用＊隔开了
def registe(name,age,*other,city,country):
    print(name,age,other,city,country)
# cathy 18 () Xian China
registe('cathy',18,city='Xian',country='China')
# cathy 18 ((1, 2, 3),) Xian China
registe('cathy',18,(1,2,3),city='Xian',country='China')
# kate 20 () Xiamen China
registe('kate',20,**extra)

#### 参数组合，上面的参数可以组合使用，但是必须确保顺序：
# 必选参数　默认参数　可变参数　命名关键字参数　关键字参数
# 注意：命名关键字参数在关键字参数前面
def f1(a,b,c=0,*change,d,**extra):
    print('a=',a,'b=',b,'c=',c,'change=',change,'d=',d,'extra=',extra)

def f2(a,b,*,d,**extra):
    print('a=',a,'b=',b,'d=',d,'extra=',extra)
# a= 1 b= 2 c= 3 change= ((3, 4),) d= abc extra= {'name': 'nick', 'age': 30}
f1(1,2,3,(3,4),d='abc',name='nick',age=30)
# 命名关键字d是不能省略的
# TypeError: f1() missing 1 required keyword-only argument: 'd'
# f1(1,2)
# a= 1 b= 2 c= 0 change= () d= 30 extra= {}
f1(1,2,d=30)

### 重点来了：任意函数参数都可以通过fun(*arg1,**arg2)来调用，不管实际的参数怎么定义
t = (1,2,3,4)
d = {'d':50,'city':'Beijing','country':'China'}
# a= 1 b= 2 c= 3 change= (4,) d= 50 extra= {'city': 'Beijing', 'country': 'China'}
f1(*t,**d)
# 因为有命名关键字参数d,所以dict d中必须有'd'
d = {'city':'Beijing','country':'China'}
# 报错：TypeError: f1() missing 1 required keyword-only argument: 'd'
# f1(*t,**d)

## 递归的使用
# 使用递归要注意防止栈溢出：函数调用是通过栈的数据结构实现的
# 每当进入一个函数调用，栈就会加一层栈帧，当函数退出，栈就减一层栈帧．
# 而栈的大小有限，如果递归层级太多(调用函数自身太多次),可能会栈溢出

# 比如使用递归计算阶乘：1*2*3*4*5...*n!
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n

# 120
print(fact(5))
# RecursionError: maximum recursion depth exceeded in comparison
# print(fact(1000))

## 防止栈溢出，可以通过尾递归优化
# 尾递归：函数返回的时候调用了函数自身（递归），return的不能是表达式，比如上面的：fact(n - 1) * n是表达式．
# 尾递归优化：当满足尾递归时，编译器会对其优化，使得不管递归调用多少次，都只会加一层栈帧
# 上面的递归函数进行改写：
def fact_iter(num,product=1):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 120
print(fact_iter(5))
# RecursionError: maximum recursion depth exceeded in comparison
# 这里仍然报错，是因为使用的python解释器并没有对尾递归进行优化
# print(fact_iter(1000))

#### 汉诺塔的移动：http://www.baike.com/wiki/%E6%B1%89%E8%AF%BA%E5%A1%94
# 三根柱子A,B,C　A上从下往上按从大到小的顺序堆了N个盘子，计算将盘子堆到另外一根柱子上（这里从A到C）所需次数，一次只能移动一个盘子
# 并且大盘子不能堆在小盘子上．
# 按照数学归纳法：1个盘子－＞１次　２个盘子－＞３次　３个盘子－＞７次　４个盘子－＞１５次...归纳出：2^n - 1次
# 找规律分析：
# 1个盘子：A-->C
# 2个盘子：A-->B A-->C B-->C
# 3个盘子：A-->C A-->B C-->B A-->C B-->A B-->C A-->C
# ...
# 过程理解：n个盘子，先从Ａ移动n-1个到Ｂ（当前过程是复杂的）;Ａ还剩下一个时，从Ａ移动到Ｃ；最后从Ｂ将n-1个移动到Ｃ
# 用递归实现：
def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

# move A --> C
move(1,'A','B','C')
# move A --> B
# move A --> C
# move B --> C
move(2,'A','B','C')
# move A --> C
# move A --> B
# move C --> B
# move A --> C
# move B --> A
# move B --> C
# move A --> C
move(3,'A','B','C')

### 递归的理解不要陷入死胡同，总结出规律，如果确认是递归问题，那么理清过程去调用函数即可，别陷太深．．．．