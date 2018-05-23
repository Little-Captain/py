#!/usr/bin/env python

# 模块目录结构
# .
# ├── setup.py
# ├── suba
# │   ├── aa.py
# │   ├── bb.py
# │   └── __init__.py
# └── subb
#     ├── cc.py
#     ├── dd.py
#     └── __init__.py

from distutils.core import setup

setup(name="模块名",
      version="版本",
      description="描述",
      author="作者",
      py_modules=['suba.aa', 'suba.bb', 'subb.cc', 'subb.dd'])

# 构建模块
# python setup.py build

# 生成发布压缩包
# python setup.py sdist

# 模块的安装和使用
# 1. 找到模块的压缩包
# 2. 解压
# 3. 进入文件夹
# 4. 执行命令 python setup.py install
# 注意: 如果在 install 的时候，执行目录安装，可以使用 python setup.py install --prefix=安装路径

# 模块的引入使用
# import
# from import

