class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset=[]
        def dfs(index):
            if sum(subset)==target:
                res.append(subset.copy())
                return
            if index>=len(nums) or sum(subset)>target:
                return
            
            #Include
            subset.append(nums[index])
            dfs(index)

            #Exclude
            subset.pop()
            dfs(index+1)

        dfs(0)
        return res

        