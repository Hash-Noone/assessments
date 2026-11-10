def memoize(f):
        cache = {}

        def wrapper(*args, **kwargs):
            key = args
            print(cache)

            if key in cache:
                return cache[key]

            result = f(*args, **kwargs)
            cache[key] = result

            return result
        return wrapper

def edit_naive(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    if a[0] == b [0]:
        return edit_naive(a[1:], b[1:])
    return 1 + min(
        edit_naive(a, b[1:]),
        edit_naive(a[1:], b),
        edit_naive(a[1:], b[1:])
    )
print(edit_naive("kitten", "sitting"))

@memoize
def edit_memo(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    if a[0] == b [0]:
        return edit_memo(a[1:], b[1:])
    return 1 + min(
        edit_memo(a, b[1:]),
        edit_memo(a[1:], b),
        edit_memo(a[1:], b[1:])
    )
    
print(edit_memo("kitten", "sitting"))