#!/usr/bin/env python
import os

folders = filter(os.path.isdir, os.listdir())
for folder in folders:
    tmp = '%s/d' % folder
    haveSub = False
    if os.path.isdir(tmp):
        os.chdir(tmp)
        
        # f = open('%s_f.podspec' % folder, 'r')
        # content = f.read()
        # content.replace('172.31.103.221', 'www.qxxlgogs.com')
        # os.system("echo \"%s\" > %s_f.podspec"%(content, folder))
        
        os.system('sed -i \"\" \"s%%172.31.103.221%%www.qxxlgogs.com%%g\" \"%s_f.podspec\"'%folder)
        
        os.chdir('../..')
        haveSub = True
    tmp = '%s/r' % folder
    if os.path.isdir(tmp):
        os.chdir(tmp)
        
        # f = open('%s_f.podspec' % folder, 'r')
        # print(folder)
        # content = f.read()
        # content.replace('172.31.103.221', 'www.qxxlgogs.com')
        # os.system("echo \"%s\" > %s_f.podspec"%(content, folder))
        
        os.system('sed -i \"\" \"s%%172.31.103.221%%www.qxxlgogs.com%%g\" \"%s_f.podspec\"'%folder)
        
        os.chdir('../..')
        haveSub = True
    if not haveSub:
        os.chdir(folder)
        
        # f = open('%s_f.podspec' % folder, 'r')
        # print(folder)
        # content = f.read()
        # content.replace('172.31.103.221', 'www.qxxlgogs.com')
        # os.system("echo \"%s\" > %s_f.podspec"%(content, folder))
        
        os.system('sed -i \"\" \"s%%172.31.103.221%%www.qxxlgogs.com%%g\" \"%s_f.podspec\"'%folder)
        
        os.chdir('..')
