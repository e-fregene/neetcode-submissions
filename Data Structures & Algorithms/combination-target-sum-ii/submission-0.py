class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        subset=[]
    
        def dfs(index):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if index>=len(candidates) or sum(subset)>target:
                return

            #Including
            subset.append(candidates[index])
            dfs(index+1)

            #exlusion
            subset.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index+=1
            dfs(index+1)

        dfs(0)
        return res