from typing import List

import pyleet


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0
        subset_sum = (total_sum + target) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to make sum = 0, by taking no elements

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]


testcases = [
    {
        "input": ([1, 1, 1, 1, 1], 3),
        "expected": 5
    },
    {
        "input": ([1], 1),
        "expected": 1
    }
]

results = pyleet.run(testcases)
pyleet.print_results(results)
