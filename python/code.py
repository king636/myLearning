#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##　编码问题
# 理解ASCII编码：127个字符，包括：大小写英文字母，数字和一些符号．一个字符占一个字节，８位．
# 理解unicode编码：中文的一个字符用一个字节无法表示，至少两个字节，比如用GB2312编码；而unicode编码则统一所有语言，包括英文，中文，日文，韩文等
# unicode编码通常２个字节，如果表示的是ASCII中的字符，前面补０即可．所以unicode编码可能导致存储空间浪费(如果ASCII字符多的时候);
# 在unicode编码基础上的utf-8编码：长度可变，在表示ASCII字符时和ASCII编码一样，只需要一个字节;
# utf-8: 在表示中文字符时，占用３个字节．这样大多情况下都使用utf-8编码即可．

## 计算机系统的编码工作方式：内存中统一用unicode编码，保存文件或传输的时候用utf-8编码(由文本编辑器或者浏览器等指定).
# 从文件读时，将utf-8转换成unicode在内存中处理，保存时又将unicode转换成utf-8
# 或者传输时转换成utf-8,比如网页源码中的<meta charset="UTF-8" />信息，表示网页的编码．

## python3的字符串以unicode编码,所以支持多语言
# ord()函数获取字符的整数表示
# 65
print(ord('A'))
# 20013
print(ord('中'))

# 报错：TypeError: ord() expected a character, but string of length 3 found
# 所以字符要么是ASCII码的字符，要么是多语言对应的字符
# print(ord('ABC'))

# chr()函数与ord()相反，把编码转换为对应的字符
# A
print(chr(65))
# 中
print(chr(20013))

# 用十六进制写字符串：中文
print('\u4e2d\u6587')

# 保存或者传输字符时，需要变为以字节为单位的bytes
# 这里是unicode编码，每个字符占２个字节
x = 'ABC'
# 'ABC'
print(x)
# 这里len()函数计算的是字符数
# 3
print(len(x))
# 这里表示的是bytes，每个字符只占一个字节
x = b'ABC'
# b'ABC'
print(x)
# 这里len()函数计算的是字节数
# 3
print(len(x))

# 再如：
# 2,字符
print(len('中文'))
# 6，字节
print(len('中文'.encode('utf-8')))

# 对字符串进行编码，转换为bytes
# b'ABC'
print('ABC'.encode('ascii'))
# b'\xe4\xb8\xad\xe6\x96\x87'
# 显示为\x**是因为该字节无法显示为ascii字符
print('中文'.encode('utf-8'))
# 报错：UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# print('中文'.encode('ascii'))

# 对bytes解码，转换为字符串
# ABC
print(b'ABC'.decode('ascii'))
# 中文
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# \xff无法解码，报错：UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 3-4: invalid continuation byte
# print(b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8'))
# 忽略解码时的错误字节,参数：errors='ignore'
# 中
print(b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8',errors='ignore'))