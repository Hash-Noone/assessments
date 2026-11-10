

def memoize(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args[0], tuple(args[1]))

        if key in cache:
            wrapper.hits += 1
            return cache[key]

        wrapper.misses += 1

        result = f(*args, **kwargs)
        cache[key] = result

        wrapper.calls += 1

        return result

    wrapper.hits = 0
    wrapper.misses = 0
    wrapper.calls = 0

    return wrapper


@memoize
def count_ways(target, nums):
    if target == 0:
        return 1

    if target < 0:
        return 0

    if not nums:
        return 0

    return (
        count_ways(target - nums[0], nums)
        + count_ways(target, nums[1:])
    )


print(count_ways(5, [1, 2, 5]))

print("Cache hits:", count_ways.hits)
print("Cache misses:", count_ways.misses)
print("Function calls:", count_ways.calls)
