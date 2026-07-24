class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums) # no duplicates

        if len(no_duplicates) == len(nums):
            return False
        else:
            return True