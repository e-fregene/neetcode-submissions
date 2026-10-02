class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(subset):
            #Base Case
            if len(subset) == len(nums):
                res.append(subset[:])
            
            for num in nums:
                #Constraint
                if num in subset:
                    continue
                
                subset.append(num)
                dfs(subset)
                subset.pop()
        dfs([])
        return res