def count_ways_dp(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
                
    return dp[target] if dp[target] else -1

def min_coins(target, coins):
    dp = [target + 1] * (target + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] <= target else -1

print(count_ways_dp(5, [1, 2, 5]))