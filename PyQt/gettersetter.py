class product(object):
    def __init__(self, name):
        self._name = name
    def set_name(self, name):
        print ('Setting product name: %s' % name)
        self._name = name
    def get_name(self):
        return self._name
    def del_name(self):
        del self._name
    name = property(get_name, set_name)
p = product('Camera')
print('Getting product name ', p.name)
p.name = 'Cell'
print('Getting product name ', p.name)
