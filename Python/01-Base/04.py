info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
# info['na']
print(info['name'])
print(info.get('na'))
print(info.get('name'))
info['na'] = 'haha'
print(info)
del info['na']
print(info)
for key, value in info.items():
    print('key %s: value %s'%(key, value))
chars = ['a', 'b', 'c', 'd']
for i, chr in enumerate(chars):
    print(i, chr)

for i, k in enumerate(info):
    print(i, k)