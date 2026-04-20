class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            tag : DP bottom -> top
            tc: O(n)
            sc: O(1)
        """
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
        