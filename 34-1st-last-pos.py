class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_last = [-1,-1]
        
        if nums == [target]:
            return [0,0]

        l, r = 0, len(nums) - 1
        not_found = True        
        while l <= r and not_found:
            m = (l + r) // 2
            print("in while loop")
            print(f"BEFORE: Left: {l}, Right: {r}. Mid: {m}")
            if nums[m] == target:
                print("found potential first")
                # check first
                if m == 0 or not nums[m - 1] == target:
                    print("FOUND FIRST")
                    first_last[0] = m
                    not_found = False
                elif nums[m - 1] == target:
                    print("Not first")
                    r = m - 1
                    # if nums[r] == target:
                    #     print("FOUND FIRST after")
                    #     first_last[0] = r
                    #     not_found = False                    
            elif nums[m] > target:
                print(f"{nums[m]} > {target}")
                r = m - 1
            elif nums[m] < target:
                print(f"{nums[m]} < {target}")
                l = m + 1
            print(f"AFTER: Left: {l}, Right: {r}. Mid: {m}")

        l, r = 0, len(nums) - 1
        not_found = True
        while l <= r and not_found:
            m = (l + r) // 2
            if nums[m] == target:
                # check last
                if m == len(nums) - 1 or not nums[m + 1] == target:
                    print("FOUND LAST")
                    first_last[1] = m
                    not_found = False
                elif nums[m + 1] == target:
                    print("Not last")
                    l = m + 1
                    # if nums[l] == target:
                    #     print("FOUND LAST after")
                    #     first_last[1] = l
                    #     not_found = False                      
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        
        return first_last if not first_last[0] == -1 and not first_last[1] == -1 else [-1,-1]
    