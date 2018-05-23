# coding:utf8

import os
from pyPdf import PdfFileWriter, PdfFileReader

def split(in_file, start, end, out_file):
    
    # 读取文件流
    input_stream = file(in_file, 'rb')
    
    # pdf 读取器
    pdf_input = PdfFileReader(input_stream)
    
    # 获取 pdf 张数
    page_count = pdf_input.getNumPages()
    
    # 校验参数
    if start < 0 or end > page_count or start >= end:
        print("页码有误")
        return
    
    # pdf 写入器
    pdf_out = PdfFileWriter()

    # 获取页面数据, 并存储
    for j in range(start, end):
        page = pdf_input.getPage(j)
        pdf_out.addPage(page)
    
    # 打开文件输出流
    out_stream = file("./" + out_file, 'wb')
    
    # 将文件流写入具体文件
    pdf_out.write(out_stream)
    
    # 关闭输出流
    out_stream.close()
    
    # 关闭读取流
    input_stream.close()

if __name__ == '__main__':
    import sys
    try:
        in_file = sys.argv[1]
        start = int(sys.argv[2])
        end = int(sys.argv[3])
        out_file = sys.argv[4]
        split(in_file, start, end, out_file)
    except:
        print("传入参数有误")