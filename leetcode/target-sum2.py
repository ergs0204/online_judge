import pyleet
testcases = [
    (([1, 1, 1, 1, 1], 3), 5),
    ((([1], 1)), 1)
]


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        before = dict()
        after = {0: 1}
        for num in nums:
            before = after
            after = dict()
            for p, c in before.items():
                after[p+num] = after.get(p+num, 0)+c
                after[p-num] = after.get(p-num, 0)+c

        return after.get(target, 0)


results = pyleet.run(testcases)
pyleet.print_results(results)
