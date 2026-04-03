class Solution:
    def climbStairs(self, n: int) -> int:
        """
            tag: dynamic programming
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        if n<= 2:
            return n # quick return
        dp = [0] * (n + 1) # start from 1
        dp[1], dp[2] = 1, 2 # init 
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] # calculate dp table
        
        return dp[n] # return
        