class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_array = set(nums)
        return len(nums) != len(new_array)
        