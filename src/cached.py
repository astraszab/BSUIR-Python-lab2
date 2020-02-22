import functools
import warnings


def cached(func):
    """Cache arguments when function is called and save the result
    to use instead of recalculating.
    """
    @functools.wraps(func)
    def caching_wrapper(*args, **kwargs):
        try:
            if (args, tuple(kwargs.items())) in cache:
                return cache[args, tuple(kwargs.items())]
            else:
                res = func(*args, **kwargs)
                cache[args, tuple(kwargs.items())] = res
                return res
        except TypeError:
            warnings.warn(
                "arguments cannot be hashed so caching is impossible.",
                RuntimeWarning)
            return func(*args, **kwargs)
    cache = {}
    return caching_wrapper
