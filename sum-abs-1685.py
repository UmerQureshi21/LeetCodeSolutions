from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre, post, result = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        sumForPre = 0
        sumForPost = 0
        for num in nums:
            sumForPre += num
            sumForPost += num
        for i, num in enumerate(nums):
            post[i] = sumForPre - num
            sumForPre = post[i]
        for i in range(len(nums)):
            temp = len(nums) - i - 1
            pre[temp] = self.abs(nums[temp] * temp - (sumForPost - nums[temp]))
            sumForPost = sumForPost - nums[temp]

        for i, num in enumerate(nums):
            result[i] = pre[i] + abs(num * (len(nums) - i - 1) - post[i])
            

        # for i, num in enumerate(nums):
        #     print(f"Num: {num}, occurences: {len(nums) - 1}, remainingSum: {totalSum - num}")
        #     result[i] = abs(num * (len(nums) - 1) - (totalSum - num))
        # return result
        return result


    def abs(self, x: int):
        return x if x >= 0 else -x
    

print(Solution().getSumAbsoluteDifferences([1,4,6,8,10]))