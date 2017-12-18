#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#正则表达式用法(与js一样)，不同的地方在于：
# 1. python中需要引用re模块，匹配的语法不同；
# 2. python的正则表达式有编译的用法
# 3. python没有全局匹配？
# * 含义说明：
# * \d 匹配数字
# * \w 匹配字母或者数字
# * \s 匹配空格
# * . 匹配任意字符
# * * 匹配任意个字符(包括０个)
# * ? 匹配０个或１个字符
# * + 匹配至少一个字符
# * {n} 匹配n个字符
# * {n,m} 匹配n-m个字符
# * 举例:\d{3}\s+\d{3,8},表示用任意个空格隔开的带区号电话号码

#  * 精确匹配，使用[]表示范围
#  * [0-9a-zA-Z\_] 匹配一个数字，字母或者下划线
#  * [0-9a-zA-Z\_]+ 匹配至少由一个数字，字母或者下划线组成的字符串
#  * [a-zA-Z\_\$][0-9a-zA-Z\_\$]* 匹配任意个由字母，下划线或$开头，后接数字，字母或者下划线组成的字符串，即变量名
#　＊ [a-zA-Z\_\$][0-9a-zA-Z\_\$]{0, 19} 限制变量名长度1-20个字符.
#  * A|B　匹配A或B
#  * ^ 表示行的开头
#  * $ 表示行的结束

# 使用,导入re模块
import re
# 使用python中的r,忽略转义的问题
reg = r'^\d{3}-\d{3,8}$'
# 匹配成功返回Match对象，否则返回None
# <_sre.SRE_Match object; span=(0, 9), match='021-34556'>
print(re.match(reg,'021-34556'))
# None
print(re.match(reg,'021 3455'))

# 只要非None则说明匹配成功
if re.match(reg,'021-34556'):
    # match ok
    print('match ok')
else:
    print('match failed')

# 切分字符串
# ['a', 'b', 'c', 'd', 'e']
print(re.split(r'[\s\,]+','a,b, c   d,,e'))

# 分组,用group在Match对象上提取子串
m = re.match(r'(\d{3})-(\d{3,5})$','010-12345')
# <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
print(m)
# ('010', '12345')
print(m.groups())
# 010-12345
print(m.group(0))
# 010
print(m.group(1))
# 12345
print(m.group(2))

# 注意：以下不匹配，但是在js中是匹配的(js中可以匹配出10-12345),语义上应该是要匹配的，010当然包括\d{2}
# None
# print(re.match(r'(\d{2})-(\d{3,5})$','010-12345'))

# 贪婪匹配与非贪婪匹配
# 默认为贪婪匹配
m = re.match(r'^(\d+)(0*)$','102300')
# ('102300', '')
print(m.groups())
# 102300
print(m.group(0))
# 无
print(m.group(1))
# 无
print(m.group(2))

# 用？改为非贪婪匹配(尽可能少的匹配)，可以匹配出后面的０
m = re.match(r'^(\d+?)(0*)$','102300')
# ('1023', '00')
print(m.groups())
# 1023
print(m.group(0))
# 00
print(m.group(1))
# 无
print(m.group(2))

## 编译：如果一个正则表达式要被重复使用很多次，那么可以预编译再使用，编译可以检查正则表达式字符串本身是否合法．
# 预编译再使用，在重复使用多次时提高效率
re_phone = re.compile(r'^(\d{3})-(\d{3,8})')
# ('010', '12345')
print(re_phone.match('010-12345').groups())
# ('021', '88888888')
print(re_phone.match('021-88888888').groups())