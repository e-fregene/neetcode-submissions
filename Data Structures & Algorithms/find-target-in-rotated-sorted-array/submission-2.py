class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0, len(nums)-1


        while r >= l:
            mid = l+ (r-l)//2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]: # not in window
                    l=mid+1 # move to other window
                else:
                    r = mid-1 # search in the window
            else:
                if target < nums[mid] or target > nums[r]: # not in window
                    r=mid-1 # move to other window
                else:
                    l = mid+1 # search in the window
        return -1
        