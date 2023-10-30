#works, ~22% runtime, 40% memory
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            middle = (high+low)//2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                low = middle + 1
            else:
                high = middle - 1
        return -1

#doesn't return index properly
'''class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1 #not there, no list remaining
        middle = len(nums) // 2 #// forces int division
        print(nums[middle])
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            return self.search(nums[middle+1:], target) #return used to avoid list unhash
        else:
            return self.search(nums[:middle], target)'''
