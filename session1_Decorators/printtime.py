"""
Exercise — a decorator which times function execution

Write 'printtime' decorator which prints
how long a function took to execute.

@printtime
def loooong():
    s = 0
    for i in range(1000000):
        s += i**2
    return s

>>> looong()
looong took 5.0323423 s
333332833333500000

>>> time.time()
>>> time.time()
1441180399.3036400
>>> time.time()
1441180400.3567457
"""

def printtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print("{} took {}".format(func.__name__, end))
        return result
    return wrapper

@printtime
def loooong():
    s = 0
    for i in range(1000000):
        s += i**2
    return s

print(loooong())
=======
import time
import functools

def printtime(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        ans = func(*args, **kwargs)
        t2 = time.time()
        print(func.__name__, 'took', t2 - t, 's')
        return ans
    return functools.update_wrapper(wrapper, func)
>>>>>>> master
