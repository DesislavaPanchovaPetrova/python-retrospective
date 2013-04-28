from collections import defaultdict, OrderedDict
import functools, itertools


def groupby(func, seq):
    grouped = defaultdict(list)
    [grouped[func(item)].append(item) for item in seq]
    return grouped


def iterate(func):
    iterated_function = lambda arg: arg
    while True:
        yield iterated_function
        iterated_function = functools.partial(\
            lambda f, *args: func(f(*args)), iterated_function)


def zip_with(func, *iterables):
    if not any(iterables):
        return
    iterators = list(map(iter, iterables))
    while True:
        args = [next(iterator) for iterator in iterators]
        yield func(*args)


def cache(func, cache_size):
    d = OrderedDict()
    def func_cached(*args):
        if args not in d:
            if len(d) >= cache_size:
                d.popitem(False)
            d[args] = func(*args)
        return d[args]
    return lambda *args: func_cached(*args)
