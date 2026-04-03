class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestLength = 0

        for num in nums:
            length = 0
            current = num
            while current in numsSet:
                length += 1
                current += 1
            longestLength = max(longestLength, length)
        
        return longestLength

                    