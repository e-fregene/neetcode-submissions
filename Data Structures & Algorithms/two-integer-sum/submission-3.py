class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target = #
        for indecie in range(len(nums)):
            found = target - nums[indecie]
            if found in nums:
                out= [nums.index(found), indecie]
        return out

        