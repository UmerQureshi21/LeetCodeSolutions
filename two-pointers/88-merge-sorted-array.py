class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = 0
        pointer2 = 0
        while pointer2 < n and pointer1 < len(nums1):
            if pointer1 < m and nums2[pointer2] > nums1[pointer1]:
                pointer1 +=1
            else:
                nums1[pointer1+1:] = nums1[pointer1:len(nums1) - 1]
                nums1[pointer1] = nums2[pointer2]
                pointer1+=1
                pointer2+=1
                m+=1
        return nums1

print(Solution().merge([-12,-11,-9,0,0,0,0,9,10,0,0,0,0,0],9,[0,1,8,9,11],5))

