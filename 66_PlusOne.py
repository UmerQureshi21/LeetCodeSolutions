class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        big_num = 0
        for i, num in enumerate(digits):
            big_num += num * 10**(len(digits) - 1 - i)
        big_num += 1
        new_digits = []
        for digit in str(big_num):
            new_digits.append(digit)
        return new_digits
    
print(Solution().plusOne([1,2,3,4,9]))