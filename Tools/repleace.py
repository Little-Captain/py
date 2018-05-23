#!/usr/bin/env python
import os

folders = filter(os.path.isdir, os.listdir())
for folder in folders:
    os.chdir(folder)
    try:
        process = os.popen('git remote -v')
        output = process.read()
        output = output.split()
        output = output[1]
        output = output.replace('172.31.103.221', 'www.qxxlgogs.com')
        os.system('git remote remove origin')
        os.system('git remote add origin %s'%output)
    except:
        pass
    os.chdir('..')
