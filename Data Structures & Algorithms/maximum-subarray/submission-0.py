class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi, curSum = nums[0], 0

        for x in nums:
            curSum = max(curSum, 0)
            curSum+= x
            maxi = max(maxi, curSum)
        return maxi
        