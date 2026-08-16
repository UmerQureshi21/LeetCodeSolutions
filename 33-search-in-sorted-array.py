from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target == nums[0]:
            return 0
        elif len(nums) == 0:
            return -1

        index = self.binarySearch(nums, target,0,len(nums) - 1)
        return index
    
    def binarySearch(self, nums, target, start, end) -> int:
        if start >= end:
            return -1
        
        mid = (start + end) // 2
        
        if nums[mid] == target:
            return mid    
        if nums[start] == target:
            return start  
        if nums[end] == target:
            return end      
        if nums[mid] <= nums[start]: # in right sorted portion
            if target > nums[mid] and target > nums[end]:
                return self.binarySearch(nums, target, start, mid)
            if target > nums[mid] and target < nums[end]:
                return self.binarySearch(nums,target,mid+1,end)
            if target < nums[mid]:
                return self.binarySearch(nums, target, start, mid)
        else: # in left sorted portion
            if target < nums[mid] and target < nums[start]:
                return self.binarySearch(nums,target,mid+1,end)
            if target < nums[mid] and target > nums[start]:
                return self.binarySearch(nums,target,start,mid)
            if target > nums[mid]:
                return self.binarySearch(nums,target,mid+1,end)
            
# neetcode perso helped me to figure out that I had to check if mid 
# was less than or greater than start to find out what sorted portion im in


if __name__ == "__main__":
    s = Solution()

    # Example test cases
    print(s.search([1], 0))
