def lru_cache(max_size):
    if max_size is None:
        max_size = float("inf")
    
    def memoize(f):
        cache = {}
        used = []

        def wrapper(*args, **kwargs):
            key = args
            if max_size == 0:
                return f(args)

            if key in cache:
                wrapper.hits += 1
                used.remove(key)
                used.append(key)
                return cache[key]

            wrapper.misses += 1

            result = f(*args, **kwargs)
            if len(cache) == max_size:
                cache.pop(used.pop(0))
            cache[key] = result
            used.append(key)

            return result

        def keys():
            return used

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.keys = keys

        return wrapper
    return memoize

def fifo_cache(max_size):
    def memoize(f):
        cache = {}

        def wrapper(*args, **kwargs):
            key = args

            if key in cache:
                wrapper.hits += 1
                return cache[key]

            wrapper.misses += 1

            result = f(*args, **kwargs)
            if len(cache) == max_size:
                first_key = next(iter(cache))
                cache.pop(first_key)
            cache[key] = result


            return result

        def keys():
            return [key for key in cache]

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.keys = keys

        return wrapper
    return memoize

@lru_cache(2)
def f(x):
    return x * x

for x in (1, 2, 1, 3, 2, 1):
    f(x)

print("Cache hits:", f.hits)
print("Cache misses:", f.misses)
print(f.keys())