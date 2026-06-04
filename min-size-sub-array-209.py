class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = nums[0]
        lengths = []
        if sum >= target:
            lengths.append(1)
        l = 0
        r = 0
        for num in nums[1:]:
            r+=1
            sum += num
            if sum >= target:
                while sum >= target:
                    sum -= nums[l]
                    l += 1
                l -= 1
                sum += nums[l]
                lengths.append((r - l + 1))
            # if sum == target:
            #     print(f"left: {l}, right: {r}")
            #     lengths.append((r - l + 1))
            # elif sum > target:
            #     while sum > target:
            #         sum -= nums[l]
            #         l += 1
            #     if sum == target:
            #         print(f"left: {l}, right: {r}")
            #         lengths.append((r - l + 1))
        if len(lengths) == 0:
            return 0
        else:
            min = lengths[0]
            for l in lengths:
                if l < min:
                    min = l
            return min