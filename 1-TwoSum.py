#works, ~47% run and ~21% mem
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        y = 0
        d = {}
        for x in nums:
            d[x] = y
            y+=1
        y=1
        for a, b in enumerate(nums):
            if ((target-b) in d) and (d[target-b] != a):
                return (a,d[target-b])

