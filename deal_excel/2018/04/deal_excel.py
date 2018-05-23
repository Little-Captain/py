#!/usr/bin/env python

import xlrd
import os

color = '#ff0000'

# 解析含有姓名的行, 并返回姓名字符串
def parseName(row):
    if type(row) != list:
        raise Exception('row 参数必须为 list')
    index = 0
    for cell in row:
        index += 1
        if cell.value == '姓 名:':
            break
    return row[index + 1].value

# 解析出打卡时间, 以元组返回
def firstAndLast(today, tomorrow):
    if tomorrow[0] == '0':
        return (today[1], today[2])
    else:
        return (today[1], tomorrow[0])

# 三段解析打卡时间, 以 list 返回
def parseTime(str):

    resultList = str.split(sep='\n')
    result = ['0' for i in range(0, 3)]

    for time in resultList:
        hourAndMinute = time.split(sep=':')
        hour = int(hourAndMinute[0])
        if hour < 6:
            result[0] = time
        elif hour < 13:
            result[1] = time
        else:
            result[2] = time

    return result

# 解析出一行的所有签到记录
def parseAttendance(row):
    if type(row) != list:
        raise Exception('row 参数必须为 list')
    attendance = [0 for i in range(0, 31)]
    tmp = [0 for i in range(0, 31)]
    for i in range(0, 31):
        if row[i].ctype == 0:
            tmp[i] = ['0', '0', '0']
        else:
            tmp[i] = parseTime(row[i].value.strip())
    for i in range(0, 31):
        if i == 30:
            attendance[i] = firstAndLast(tmp[i], ['0', '0', '0'])
        else:
            attendance[i] = firstAndLast(tmp[i], tmp[i+1])
    return attendance

# 解析出一个员工的所有信息
def parseOne(rows):
    if type(rows) != list:
        raise Exception('rows 参数必须为 list')
    return (parseName(rows[0]), parseAttendance(rows[1]))

# 针对上午的打卡进行解析
def parseAM(time):
    hourAndMinute = time.split(sep=':')
    hour = int(hourAndMinute[0])
    if hour == 0:
        return '<font color=%s>' % color + time + '</font>' + '<br>'
    minute = int(hourAndMinute[1])
    if hour >= 9 and minute >= 1:
        return '<font color=%s>' % color + time + '</font>' + '<br>'
    else:
        return time + '<br>'

# 针对下午的打卡进行解析
def parsePM(time):
    hourAndMinute = time.split(sep=':')
    hour = int(hourAndMinute[0])
    if hour == 0:
        return '<font color=%s>' % color + time + '</font>'
    if hour < 18:
        return '<font color=%s>' % color + time + '</font>'
    else:
        return time

# 提供给外界调用的函数
# xlsFile      : 输入的 Excel 文件
# mdFile       : 输出的 Markdown 文件
# weekPosition : 这个月1号开始的位置 对应关系为 Sun(0) Mon(1) Tues(2) Wed(3) Thur(4) Fri(5) Sat(6)
def writeToMd(xlsFile, mdFile, weekPosition):
    if not ((type(weekPosition) == int) and (weekPosition >= 0) and (weekPosition <= 6) and (type(xlsFile) == str) and (type(mdFile) == str)):
        raise Exception('xlsFile、mdFile 为文件名字符串, weekPosition 参数必须为 int 且在区间 [0, 6] 内')
    # 打开 Markdown 文件准备写入
    fp = open(os.getcwd() + '/' + mdFile, 'w', encoding='utf8')
    # 打开 Excel 文件
    data = xlrd.open_workbook(os.getcwd() + '/' + xlsFile)
    # 获取打卡记录 sheet
    attendanceSheet = data.sheet_by_name('刷卡记录')
    nrows = attendanceSheet.nrows
    rows = [attendanceSheet.row(index) for index in range(4, nrows)]
    for i in range(2, len(rows) + 1, 2):
        (name, attendance) = parseOne([rows[i-2], rows[i-1]])
        if name in ['母满全', '黎雪萍', '张晗', '赵佩', '廖泰', '唐玉龙', '崔云飞', '张晨曦', '徐健', '旦福曼']:
            continue
        fp.write(name + '\n')
        fp.write('=====\n\n')
        fp.write('|Sun.|Mon.|Tues.|Wed.|Thur.|Fri.|Sat.|\n')
        fp.write('|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n')
        if weekPosition <= 4:
            attendance = [('0', '0') for i in range(0, weekPosition)] + attendance + [('0', '0') for i in range(0, 4 - weekPosition)]
        else:
            attendance = [('0', '0') for i in range(0, weekPosition)] + attendance + [('0', '0') for i in range(0, 11 - weekPosition)]
        count = len(attendance)
        position = 0
        for i in range(1, int(len(attendance) / 7) + 1):
            subattendance = attendance[7*(i-1):7*i]
            line = ''
            for j in range(0, 7):
                elm = subattendance[j]
                line += '|'
                if position >= weekPosition and position < weekPosition + 31:
                    line += '<font color=#0000ff>' + str(position + 1 - weekPosition) + '</font>' + '<br>'
                line += '%s' % (parseAM(elm[0]) + parsePM(elm[1]))
                position = position + 1
            line += '|\n'
            fp.write(line)
    fp.close()

if __name__ == '__main__':
    xlsFile = input('Excel 文件名:\n')
    mdFile = input('Markdown 文件名:\n')
    weekPosition = int(input('本月1号是星期几:\n'))
    writeToMd(xlsFile, mdFile, weekPosition)