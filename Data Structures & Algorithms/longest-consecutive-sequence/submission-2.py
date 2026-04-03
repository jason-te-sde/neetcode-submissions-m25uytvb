class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        longestLength = 0
        currentLength = 0
        i = 0
        currentNum = 0

        while i < n:
            if currentNum != nums[i]:
                currentNum = nums[i] 
                currentLength = 0
            while i < n and nums[i] == currentNum:
                i += 1
            currentLength += 1
            currentNum += 1
            longestLength = max(longestLength, currentLength)
        
        return longestLength
            

            

        

                    