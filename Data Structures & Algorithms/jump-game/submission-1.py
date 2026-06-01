class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        step = nums[0]

        for i in range(len(nums)):
            if step >= i:
                step = max(step, i + nums[i])
            if step >= len(nums) - 1:
                return True
        return False