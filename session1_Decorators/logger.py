import functools


def logger(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(
            "{0} is called with args {1} kwargs {2}".format(f.__name__,
                                                            list(args),
                                                            kwargs))
        result = f(*args, **kwargs)
        print("{} returns {}".format(f.__name__, result))
        return result

    return wrapper


@logger
def f(x, y):
    return g(x) + g(y)


@logger
def g(x):
    return 2 * x

# f is called with args [5, 6] kwargs {}
# g is called with args [5] kwargs {}
# g returns 10
# g is called with args [6] kwargs {}
# g returns 12
# f returns 22
# f(5, 6)
