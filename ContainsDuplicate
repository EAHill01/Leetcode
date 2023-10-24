#worked, very memory efficient but slow
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        dex = 0
        while dex != len(nums)-1:
            if nums[dex]==nums[dex+1]:
                return True
            dex+=1
        return False
        
#works, but exceeded time constraints
"""class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dex = 1
        for x in nums:
            if x in nums[dex:]:
                return True
            dex+=1
        return False
        """
