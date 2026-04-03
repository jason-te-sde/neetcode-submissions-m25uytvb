class Solution:
    def climbStairs(self, n: int) -> int:
        """
            tag: dynamic programming
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        one, two = 1, 1 # init

        for i in range(n - 1): # swap and update
            temp = one 
            one = one + two
            two = temp
        
        return one