class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # step1 : count numbers appered times in nums
        # step2 : put numbers in bucket base on times
        # step3 : add the most K Frequent Elements
        count = {}
        frequency =[[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, freq in count.items():
            frequency[freq].append(num)
        res = []
        for i in range(len(frequency) - 1 , 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res

            
        