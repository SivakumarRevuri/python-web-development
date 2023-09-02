class Test:
    def pprint(self, msg):
        self.msg = msg
        print(self.msg)
    
    @staticmethod
    def stat_meth(a,b):
        print('this is static method!!!', a,b)

t = Test()
t.pprint('instatnce method!')
Test.stat_meth(10,20)
t.stat_meth(20,30)

print('*'*20)

count = 0
def decor(func):
    global count
    count += 1
    print('inside decor', count)
    def inner(*args, **kwargs):
        print('inner func', count)
        return func(*args, **kwargs)
    return inner

@decor
@decor
@decor
def hello():
    print('say hello')

hello()

print('*'*20)

def fib(num: int):
    a, b = 0, 1
    while a <= num:
        yield a
        a, b = b, a+b

print(list(fib(20)))