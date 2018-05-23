#!/anaconda3/bin/python

import eyed3
import os

allfiles = []
for filename in os.listdir('./'):
    tmp = filename.split('.')
    if filename.split('.')[-1] == 'mp3':
        allfiles.append(filename)

def time_info(filename, i):
    mp3 = eyed3.load(filename)
    time_secs = mp3.info.time_secs
    return "%02d.%02d.%02d.mp3"%(time_secs // 60, time_secs % 60, i)

count = len(allfiles)
for i in range(0, count):
    oldname = allfiles[i]
    newname = time_info(oldname, i)
    os.rename(oldname, newname)