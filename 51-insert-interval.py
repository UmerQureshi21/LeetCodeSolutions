class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_intervals = []
        if len(intervals) == 0:
            return [newInterval]
        not_merged = True
        i = 0
        while i < len(intervals):
            if intervals[i][1] >= newInterval[0] and not_merged:
                print("start merge")
                temp = i + 1
                start_of_merge = intervals[i]
                end_of_merge = intervals[i]
                while temp < len(intervals) and newInterval[1] >= intervals[temp][0]:
                    end_of_merge = intervals[temp]
                    temp += 1
                merged_interval = [start_of_merge[0],max(newInterval[1],end_of_merge[1])]
                new_intervals.append(merged_interval)  
                i = temp - 1
                not_merged = False
            else:
                print("merge ended")
                new_intervals.append(intervals[i])
            i += 1
        
        return new_intervals.append(newInterval) if not_merged else new_intervals




intervals = [[1,5]]
newInterval = [6,8]

print(Solution().insert(intervals,newInterval))