class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_val = 0

        #width= index1-index2, vals. height = min(val1, val2)

        while r > l:
            width = r - l
            height = min(heights[l], heights[r])
            max_val = max(max_val, width * height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_val
        