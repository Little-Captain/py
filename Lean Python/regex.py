import urllib.request
import re

response = urllib.request.urlopen('http://www.baidu.com')
data1 = str(response.read())

regex = '<a\s[^>]*href\s*=\s*\"([^\"]*)\"[^>]*>(.*?)</a>'

pm = re.compile(regex)
matches = pm.findall(data1)

for m in matches:
    ms=''.join(('Link: "',m[0],'" Text: "',m[1],'"'))
    print(ms)