from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x : x[0])
    initialLen = len(intervals)
    exit = False
    i = 0
    while i + 1 < initialLen:
        if(i + 1 >= len(intervals)):
            break
        if intervals[i][1] >= intervals[i+1][0]:
            while( i + 1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]):
                newInterval = [intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                intervals.pop(i + 1)
                intervals.pop(i)
                intervals.insert(i,newInterval)
                print(f"Intervals: {intervals}")
                print(f"new lenght acuta: {len(intervals)}, i: {i}")
                if (i + 1 >= len(intervals)):
                    print("EXIT BECOMES TRUE")
                    exit = True
            print("Out of while")
        print("Hello")
        if (exit):
            print("HELLO")
            break
        i += 1
    return intervals
        
        
        
        
    
print(merge([[4,7],[1,4]]))   
#print(merge([[0,50],[29,30],[40,56],[50,51],[56,60],[62,70]]))