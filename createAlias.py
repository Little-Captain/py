#!/anaconda3/envs/py3.6/bin/python

import os

allApps = []
for app in os.listdir('/Applications/.'):
    tmp = app.split('.')
    if app.split('.')[-1] == 'app':
        allApps.append(app)

for app, i in zip(allApps, range(0, len(allApps))):
    allApps[i] = 'alias %s="open /Applications/%s"\n' % (app.split('.')[0].lower().replace(" ", ""), app.replace(" ", "\ "))

fp = open('alias.txt', "w")
fp.writelines(allApps)
fp.close()