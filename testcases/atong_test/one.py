# 描述符类
class revealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        print("updating", self.name)
        self.val = val


class myClass:
    x = revealAccess(10, 'var "x"')
    y = 5


m = myClass()
print(m.x)
m.x = 20
print(m.x)
print(m.y)
