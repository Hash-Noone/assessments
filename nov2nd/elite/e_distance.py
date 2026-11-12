def memoize(f):
        cache = {}

        def wrapper(*args, **kwargs):
            key = args

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


def edit_table(a, b):
    rows = len(a) + 1
    cols = len(b) + 1

    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        dp[i][0] = i

    for j in range(cols):
        dp[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):

            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )

    return dp[-1][-1]

def edit_table_optimized(a, b):
    prev = list(range(len(b) + 1))

    for i in range(1, len(a) + 1):
        curr = [i] + [0] * len(b)

        for j in range(1, len(b) + 1):

            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1]

            else:
                curr[j] = 1 + min(
                    prev[j],      # Delete
                    curr[j - 1],  # Insert
                    prev[j - 1]   # Replace
                )

        prev = curr

    return prev[-1]