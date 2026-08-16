from typing import List

'''
O(n^2) solution

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer = [0]*len(temperatures)
    
    for i in range(len(temperatures)):
        count = 1
        flag = True
        for j in range(i + 1, len(temperatures)):
            if (temperatures[j] > temperatures[i] and flag):
                answer[i] = count
                flag = False
            else:
                count+=1
    
    
    return answer
'''


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answers = [0]*len(temperatures)
    stack = []
    
    def stackItem (temp,days,index):
        return {"temp":temp,"days":days,"index":index}

    for i, temp in enumerate(temperatures):
        if i == 0 or (i > 0 and temp <= temperatures[i-1]):
            stack.append(stackItem(temp,0,i))
        else:
            popCount = 0
            while len(stack) > 0 and temp > stack[-1]["temp"]:
                popCount += 1   
                stack[-1]["days"] = stack[-1]["days"] + popCount
                answers[stack[-1]["index"]] = stack[-1]["days"]
                stack.pop()
            if len(stack) > 0:
                stack[-1]["days"] = popCount 
            stack.append(stackItem(temp,0,i))

    return answers



print(dailyTemperatures([63,62,60,59,58,57,56,61,80]))