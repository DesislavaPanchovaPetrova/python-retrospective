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
    if cache_size <= 0:
        return func

    cached_calls = OrderedDict()
    def func_cached(*args):
        if args not in cached_calls:
            if len(cached_calls) >= cache_size:
                cached_calls.popitem(False)
            cached_calls[args] = func(*args)
        return cached_calls[args]
    return lambda *args: func_cached(*args)
