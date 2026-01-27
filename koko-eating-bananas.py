from typing import List 
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        m = (l + r) // 2
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        while l <= r:
            # print(f"in while: {l}, {m}, {r}")
            m = (l + r) // 2
            if self.isValid(piles,m,h):
                # print("was valid, going lower")
                r = m - 1
            else:
                # print("wasn't valid, going higher")
                l = m + 1
        # print(f"{l}, {m}, {r}")
        finals = [self.isValid(piles,l,h),self.isValid(piles,m,h),self.isValid(piles,r,h)]
        for i,speed in enumerate(finals):
            if speed:
                if i == 0:
                    return l
                elif i == 1:
                    return m
                elif i == 2:
                    return r


    def isValid(self, piles: List[int], eatingSpeed: int, h: int) -> bool:
        amountVisited = 1
        for pile in piles:
            if h == 0:
                return False
            if eatingSpeed*amountVisited >= pile:
                h -= amountVisited
            else:
                while eatingSpeed*amountVisited < pile:
                    amountVisited += 1
                h -= amountVisited
        return h >= 0


piles = [312884470]
h = 312884469



print(Solution().minEatingSpeed(piles,h))
        