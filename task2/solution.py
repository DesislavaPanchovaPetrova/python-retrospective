from collections import defaultdict

def groupby(func,seq):
    res = defaultdict(list)
    [res[func(x)].append(x) for x in seq]
    return res

import functools

def iterate(func):
    key = lambda x: x
    while True :
        yield key
        key = functools.partial(lambda f,*args: func(f(*args)), key)

import itertools

def zip_with(func, *iterables):
    iterators = list(map(iter,iterables))
    return [func(*tuple([next(iterator) for iterator in iterators]))
            for i in range(min(map(len,list(iterables))))]

from collections import OrderedDict

def cache(func , cache_size):
    def func_cached(x , d = OrderedDict()):
        if x not in d.keys():
            if len(d) >= cache_size :
                d.popitem(False)
            d[x] = func(x)
        return d[x]
    return lambda x: func_cached(x)

