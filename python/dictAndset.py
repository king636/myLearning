#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python的dict类似于js的对象
dict = {
    'name':'Nick',
    # NameError: name 'address' is not defined
    # address:'Xiamen',
    'age':30
}
# {'name': 'Nick', 'age': 30}
print(dict)
# Nick
print(dict['name'])

# 报错：NameError: name 'name' is not defined
# print(dict[name])
# AttributeError: 'dict' object has no attribute 'name'
# js中可以这样访问属性
# print(dict.name)

## 对比，js更灵活，python比较严格但是不容易出错
dict['name'] = 'Bob'
# Bob
print(dict['name'])

# key不存在，报错：KeyError: 'address'
# print(dict['address'])
# 可以增加属性，与js相同
dict['address'] = 'Shanghai'
# Shanghai
print(dict['address'])

## 判断属性是否存在，用get(),不存在返回None
# get name
if dict.get('name'):
    print('get name')
else:
    print('get None')

# get single:None
if dict.get('single'):
    print('get single')
else:
    print('get single: None')

# get()获取属性值可以带默认值
# -1
print(dict.get('single', -1))

# 删除dict中的key,用pop()．js中直接调用delete xxx.属性;
dict.pop('name')
# {'age': 30, 'address': 'Shanghai'}
print(dict)

# dict相对list来说，占用内存多，但是查找非常快．key必须不可变，不用能list作为key
list = [1,2,3]
# TypeError: unhashable type: 'list'
# dict[list] = 'a list'

#### set与dict类似，但是不存储value.也不支持可变对象
## python的dict和set,就和js的Object,Map以及Set很类似．
## python的set与js的Set用法基本相同，区别在于两个地方：
# 1. js中，var set = new Set([1,2,3]); 而python是　s = set([1,2,3])
# 2. 删除key时，python用remove(key);而js用delete(key)
# 3. python的dict和set的key都不能是list;而js中key可以是数组
s = set([1,2,3])
# {1, 2, 3}
print(s)
# add的用法与js相同
s.add('abc')
# {1, 2, 3, 'abc'}
print(s)
s.remove(3)
# {1, 2, 'abc'}
print(s)

####### python对比js,python使用dict和set;而js使用了对象，Map和Set,目前暂不知道什么情况要用Map而对象不满足？
####### js更灵活，但不容易掌握；python严格，但容易理解