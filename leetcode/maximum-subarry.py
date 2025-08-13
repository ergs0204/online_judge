class Solution:
    def maxSubArray(self, nums):
        def div(nums):
            if len(nums) == 1:
                return nums[0]
            mid = len(nums) // 2
            left = div(nums[:mid])
            right = div(nums[mid:])
            cross = cross_sum(nums, mid)
            return max(left, right, cross)

        def cross_sum(nums, mid):
            left_sum = float('-inf')
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid - 1, -1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
            current_sum = 0
            for i in range(mid, len(nums)):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
            return left_sum + right_sum
        return div(nums)
