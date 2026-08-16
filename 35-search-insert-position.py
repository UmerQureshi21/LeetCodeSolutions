class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        elif len(nums) == 1:
            if target == nums[0]:
                return 0
            elif target < nums[0]:
                return 0
            return 1
        elif len(nums) == 2:
            if target == nums[0]:
                return 0
            elif target == nums[1]:
                return 1
            elif target > nums[1]:
                return 2
            elif target < nums[0]:
                return 0
            return 1
        right = len(nums) - 1
        left = 0
        while right > left:
            middle = (right + left) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle
            elif target == nums[middle]:
                return middle
        print("middle: ",middle, "left: ", left, "right ", right )
        if target < nums[left]:
            return left
        return left + 1
    


print(Solution().searchInsert([1,3],3))