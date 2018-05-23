#!/Users/qxxl007/miniconda3/envs/py3/bin/python
import os

folders = filter(os.path.isdir, os.listdir())
for folder in folders:
    tmp = '%s/d'%folder
    haveSub = False
    if os.path.isdir(tmp):
        os.chdir(tmp)
        os.system('echo %s beginning'%tmp)
        os.system('./upload.sh')
        os.system('echo %s ended'%tmp)
        os.chdir('../..')
        haveSub = True
    tmp = '%s/r'%folder
    if os.path.isdir(tmp):
        os.chdir(tmp)
        os.system('echo %s beginning'%tmp)
        os.system('./upload.sh')
        os.system('echo %s ended'%tmp)
        os.chdir('../..')
        haveSub = True
    if not haveSub:
        os.chdir(folder)
        os.system('echo %s beginning'%folder)
        os.system('./upload.sh')
        os.system('echo %s ended'%folder)
        os.chdir('..')
