class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U: array nums, int k(return the # of most freq nums)

        k=1 return most frequent, 
        k=2 2 most frequent

        Plan: Count frequency of numbers in num.
        find way to go through those frequncyies and return k most

        match: dictionary hashmap
        """
        count = {}
        freq_array = [[] for x in range(len(nums) +1)]

        for num in nums:
            count[num] = 1+ count.get(num, 0)
        for kk, v in count.items():
            freq_array[v].append(kk)

        res = []
        for x in range(len(freq_array)-1, 0, -1):
            for one in freq_array[x]:
                res.append(one)
                if len(res) == k:
                    return res  
        
