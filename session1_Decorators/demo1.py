import warnings
import functools

warnings.simplefilter('always', DeprecationWarning)


def outdated_func():
    """
    Outdated function
    """
    warnings.warn('This is a deprecated function', DeprecationWarning,
                  stacklevel=3)


def deprecated(func):
    print 'before wrapper'

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print 'This function is deprecated'
        result = func(*args, **kwargs)
        print 'But is still running'
        return result

    print 'after wrapping'
    return wrapper


@deprecated
def myfunction(a, b, c=1):
    print 'a={0}, b={1}, c ={2}'.format(a, b, c)
    return 1

print myfunction(5, 6, 9)
# wrapper(myfunction)
