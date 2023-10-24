#worked, less memory efficient but 100ms faster
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupe = {}
        for x in nums:
            if x in dupe:
                return True
            else:
                dupe[x] = True #x is key
        return False


#worked, very memory efficient but slow
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(len(nums)-1):
            if nums[x]==nums[x+1]:
                return True
        return False


#worked, but exceeded time constraints
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dex = 1
        for x in nums:
            if x in nums[dex:]:
                return True
            dex+=1
        return False
        
