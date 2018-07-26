#!/usr/bin/env python

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
# 获取剪贴板的文字
text = pyperclip.paste()

# 处理
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

# 将处理结果拷贝到剪贴板
pyperclip.copy(text)