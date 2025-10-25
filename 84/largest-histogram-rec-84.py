from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    areas: List[int] = []
    stack: List[dict] = []
    
    for i, h in enumerate(heights):
        #continue if h equal heights[i-1]
        if i == 0 or h > heights[i-1] :
            stack.append({"height": h, "start": i})
        elif h < heights[i-1] :
            temp = None
            while len(stack) > 0 and h < stack[-1]["height"]:
                temp = stack.pop()
                areas.append(temp["height"]*(i - temp["start"]))
            stack.append({"height": h, "start": temp["start"]})
    
    while len(stack) > 0:
        temp = stack.pop()
        areas.append(temp["height"]*(len(heights) - temp["start"]))
    return max(areas)

#HOLLTTTTTT THIS TOOK ME SO LINOG B UT I GOT IT TTTTTT YEDDDIR

print(largestRectangleArea([2,1,5,6,2,3])) 
