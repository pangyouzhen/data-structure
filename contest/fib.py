def fn(x):
    if x < 2:
        return 1
    return fn(x - 1) + fn(x - 2)


from functools import lru_cache


@lru_cache
def fn(x):
    if x < 2:
        return 1
    return fn(x - 1) + fn(x - 2)
