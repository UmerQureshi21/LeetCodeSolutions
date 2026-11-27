class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''
        val_count = 0
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = '_'
                val_count +=1
        '''
        if len(nums) == 2:
            if nums[0] == nums[1] and nums[0] == val:
                nums = []
                return 0
            if nums[0] == nums[1] and nums[1] != val:
                return 0
            if nums[0] == val:
                nums[0],nums[1] = nums[1],nums[0]
                return 1
            if nums[0] != val and nums[1] != val:
                return 2
        val_count = 0
        for num in nums:
            if num == val:
                val_count +=1
        
        right = len(nums) - 1
        left = 0
        while right > left:
            if nums[right] == val:
                right -= 1
            if nums[left] != val:
                left += 1
            if right > left and nums[left] == val and nums[right] != val:
                nums[left],nums[right] = nums[right],nums[left]
                right -= 1
                left += 1

        return len(nums) - val_count, nums
    
    
print(Solution().removeElement([4,4,0,1,0,2],0))