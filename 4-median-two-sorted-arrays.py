class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A = nums1 if len(nums1) <= len(nums2) else nums2
        B = nums1 if len(nums1) > len(nums2) else nums2
        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2# index of mid point of B
            
            Aleft = 
            
        # left_partition_len = total // 2
        # left partition is going to be made up of portion 
        # of A and B, the length of the portion of A 
        # # one is going to be [0,len(A)]. do BS on this. EDGE: len(A) >= left_partition_len
        
        # start = 0
        # end = left_partition_len
        # left_A_len = (start + end) // 2
        # left_B_len = left_partition_len - left_A_len
        
        # def isValid(A,B):
        #     return left_B_len < len(B) and left_B_len >= 0 and left_A_len < len(A) and left_A_len >= 0 and A[left_A_len - 1] <= B[left_B_len] and B[left_B_len - 1] <= A[left_A_len]        
        
        # while not isValid(A,B):
        #     if B[left_B_len - 1] > A[left_A_len]:
        #         start = left_A_len + 1
        #     elif A[left_A_len - 1] > B[left_B_len]:
        #         end = left_A_len - 1
        #     left_A_len = (start + end) // 2
        #     left_B_len = left_partition_len - left_A_len
                    
        # return (max(A[left_A_len - 1], B[left_B_len - 1]) + min(A[left_A_len],B[left_B_len])) / 2 if total % 2 == 0 else min(A[left_A_len],B[left_B_len])

        

        
        
        
        
    
    
    # def getMedian(self, nums: list[int]) -> float:
    #     length = len(nums)
    #     if length % 2 == 1:
    #         return nums[length // 2]
    #     return (nums[length // 2] + nums[length // 2 - 1]) / 2
    
    

print(Solution().findMedianSortedArrays([1,2,3,6,7,9,20],[4,5,6]))


