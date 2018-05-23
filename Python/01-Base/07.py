#!/usr/bin/env python
oldFileName = input('请输入文件名')
oldFile = open(oldFileName, 'r')

if oldFile:
    fileFlagNum = oldFileName.rfind('.')
    if fileFlagNum > 0:
        fileFlag = oldFileName[fileFlagNum:]

    newFileName = oldFileName[:fileFlagNum] + '[复制]' + fileFlag

    newFile = open(newFileName, 'w')

    for lineContent in oldFile.readlines():
        newFile.write(lineContent)

    oldFile.close()
    newFile.close()
