class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farest = 0
        
        for i in range(len(nums) - 1):
            farest = max(farest, i + nums[i])
            if farest <= i:
                return False
        return True
