class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers) - 1

        while high > low:
            curr= numbers[high]+numbers[low]

            if curr > target:
                high-=1
            elif curr < target:
                low+=1
            else:
                return [low+1,high+1]

        #[1,2,3,4,5] target=4, mid=3. found = 4-3=1