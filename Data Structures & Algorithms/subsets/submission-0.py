class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        subset=[]
        def dfs(index):
            #Base case
            if index >= len(nums):
                res.append(subset.copy())
                return

            # Decision include nums[index]
            subset.append(nums[index])
            dfs(index+1)


            #Decision exclude nums[index]
            subset.pop()
            dfs(index+1)

        dfs(0)
        return res

            


        