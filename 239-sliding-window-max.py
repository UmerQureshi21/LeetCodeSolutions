from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        dq = deque()
        nums = self.getIndicesAndKthBiggest(nums)
        result = []
        nums_len = len(nums)
        
        for i in range(k):
            curr = nums[i]["biggest"]
            if not dq or dq[-1]["biggest"] >= curr:
                dq.append(nums[i])
            elif dq and dq[0]["biggest"] < curr:
                dq.appendleft(nums[i])
            elif dq:
                while curr < dq[0]["biggest"]:
                    dq.popleft()
                dq.appendleft(nums[i])
        #first append to result
        result.append(dq[-1])
        
        for i, val in enumerate(nums[k:]):
            rp = i + k 
            while dq and dq[0]["idx"] <= i:
               dq.popleft()
            while dq and dq[-1]["idx"] <= i:
                dq.pop()
            curr = nums[rp]["biggest"]
            if not dq or dq[-1]["biggest"] >= curr:
                dq.append(nums[rp])
            elif dq and dq[0]["biggest"] < curr:
                dq.appendleft(nums[rp])
            elif dq:
                while curr < dq[0]["biggest"]:
                    dq.popleft()
                dq.appendleft(nums[rp])
            result.append(dq[-1])
                
        # biggest_line = ", ".join(str(d["biggest"]) for d in dq)
        # idx_line = ", ".join(str(d["idx"]) for d in dq)

        # print(biggest_line)
        # print(idx_line)
        result = [d["value"] for d in result]
        return result
        # return result
        
        
        # maxs = []

        # for i in range(len(nums) - k + 1):
        #     window = nums[i: (i + k)]
        #     biggest = float('-infinity')
        #     for num in window:
        #         if num > biggest:
        #             biggest = num
        #     maxs.append(biggest)
        # return maxs
        
    def getIndicesAndKthBiggest(self, nums: List[int]) -> List[dict]:
        # Create list with value and original index
        nums_with_indices = [
            {"biggest": 0, "idx": i, "value": num}
            for i, num in enumerate(nums)
        ]
        
        # Sort by value in DESCENDING order (biggest first)
        sorted_by_value = sorted(nums_with_indices, key=lambda x: x["value"], reverse=True)
        
        # Assign ranks based on distinct values
        current_rank = 0
        prev_value = None
        
        for val_dict in sorted_by_value:
            # If value is different from previous, increment rank
            if val_dict["value"] != prev_value:
                current_rank += 1
                prev_value = val_dict["value"]
            
            val_dict["biggest"] = current_rank
        
        return nums_with_indices
    
nums = [3,0,1,2,2,5,4,2,10,12,13,2,6,8,8,20]
# nums = [20,20,21,19,12,23,20]
k = 4

print(Solution().maxSlidingWindow(nums, k))