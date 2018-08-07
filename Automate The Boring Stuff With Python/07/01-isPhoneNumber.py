#!/usr/bin/env python

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('412-123-1232 is a phone number:')
print(isPhoneNumber('412-123-1232'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('my number is 513-123-1231.')
print('Phone number found: ' + mo.group())

# Python 中使用正则表达式的步骤:
# 1. 导入模块, import re
# 2. 用 re.compile()函数创建一个 Regex 对象. 需要使用原始字符串
# 3. 向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象
# 4. 调用 Match 对象的 group()方法，返回实际匹配文本的字符串

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 413-123-4512')
print(mo.group(1))
print(mo.group(2))
print(mo.group())
print(mo.groups())

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# 用管道匹配多个分组
# 如果需要匹配真正的管道字符，就用倒斜杠转义，即 \|
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())
# 利用 findall()方法，可以找到“所有”匹配的地方

# 指定一次前缀
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# 用问号实现可选匹配
# 字符?表明它前面的分组在这个模式中是可选的(0或1次)
# 如果需要匹配真正的问号字符，就使用转义字符\?
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# 用星号匹配零次或多次(0或n次)
# \*, 匹配真正的星号字符
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3.group())

# 用加号匹配一次或多次
# \+, 匹配真正的加号字符
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

# 用花括号匹配特定次数
# (Ha){3} <=> (Ha)(Ha)(Ha)
# (Ha){3,5} <=> ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
# (Ha){3,} : [3, +oo)
# (Ha){,5} : [0, 5]

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)

# 贪心和非贪心匹配
# Python 的正则表达式默认是“贪心”的
# 在有二义的情况下, 它们会尽可能匹配最长的字符串
# 花括号的“非贪心”版本匹配尽可能最短的字符串: 即在结束的花括号后跟着一个问号
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# 问号在正则表达式中可能有两种含义
# 1. 声明非贪心匹配
# 2. 表示可选的分组

# findall() 方法
# 返回一组字符串，包含被查找字符串中的所有匹配

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
all = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(all)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
all = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(all)

# 作为 findall()方法的返回结果的总结
# 1. 如果调用在一个没有分组的正则表达式上.
# 方法findall()将返回一个匹配字符串的列表
# 2. 如果调用在一个有分组的正则表达式上.
# 方法findall()将返回一个字符串的元组的列表(每个分组对应一个字符串)

# 字符分类
xmasRegex = re.compile(r'\d+\s\w+')
all = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(all)

xmasRegex = re.compile(r'((\d+)\s(\w+))')
all = xmasRegex.findall('12\ndrummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(all)
