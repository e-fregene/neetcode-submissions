class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}
        for index in range(len(nums)):
            found = target - nums[index]
            if found in array:
               return [array[found], index]
            array[nums[index]] = index