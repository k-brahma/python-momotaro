def decorate(fun):
    def _decorated_fun(*args, **kwargs):
        mystr='計算結果は: {}'.format(fun.__name__)
        print(mystr)
        retval ='計算結果は: ' + mystr( fun(*args, **kwargs)) + ' です'
        return retval
    return _decorated_fun

def myfunc1(arg):
    return arg*3

def mydecorator(func):
    def inner(arg):
        return func(arg)

@decorate
def myfunc2(arg):
    return arg*7

print(myfunc2(7))