class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        alr_checked = []
        for i,num in enumerate(nums):
            if num in alr_checked:
                nums[i] = "_"
            else:
                alr_checked.append(num)
        for i, num in enumerate (alr_checked):
            count = 0
            for j, num2 in enumerate(nums[i+1:]):
                if num2 != "_":
                    count += 1
                if count == 1 and num2 != "_":
                    nums[j + i + 1],nums[i + 1] = nums[i + 1],nums[j + i + 1]                    
        return len(alr_checked)
    

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))