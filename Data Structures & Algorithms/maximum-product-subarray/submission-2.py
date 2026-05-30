class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMin, curMax = nums[0], nums[0]

        for num in nums[1:]:
            tempMax = curMax

            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, num * tempMax, num * curMin)

            res = max(res, curMax)

        return res