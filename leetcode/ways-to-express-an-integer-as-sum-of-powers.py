class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        memo = {}
        maxn = int(n**(1/x))

        def dfs(target, cur):
            if (target, cur) in memo:
                return memo[(target, cur)]
            if target == 0:
                return 1
            if target < 0 or cur == 0:
                return 0
            memo[(target, cur)] = (dfs(target, cur-1) +
                                   dfs(target-cur**x, cur-1)) % 1000000007
            return memo[(target, cur)]
        return dfs(n, maxn)
