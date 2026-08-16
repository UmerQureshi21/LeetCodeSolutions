from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix) * len(matrix[0]) - 1
        res = self.bs(matrix,0,length,target)
        return matrix[res[0]][res[1]] == target and res != (-1,-1)
        

    def abs(self,x):
        return x if x >= 0 else -x
    
    def bs(self, matrix: List[List[int]], start: int, end: int, target: int):
        cols = len(matrix[0])
        (srow, scol) = self.mapTo(start, cols)
        (erow, ecol) = self.mapTo(end, cols)
        (mrow, mcol) = self.mapTo((start + end) // 2, cols)


        if erow == srow:
            col = self.bs2(matrix[erow],scol,ecol,target)
            if col == -1:
                return (-1,-1)
            return (erow,col)
        if self.abs(start - end) == len(matrix) * len(matrix[0]) or self.abs(start - end) == 0:
            return (-1,-1)
        if matrix[mrow][mcol] == target:
            print("Found!!!!")
            return (mrow,mcol)
        if matrix[erow][ecol] == target:
            print("Found!!!!")
            return (erow,ecol)
        if matrix[srow][scol] == target:
            print("Found!!!!")
            return (srow,scol)        
        if matrix[mrow][mcol] > target:
            print("Bigger than target")
            print(f"start: {start}, end: {end}")
            return self.bs(matrix, start,(mrow*cols + mcol) - 1,target)
        if matrix[mrow][mcol] < target:
            print("Smaller than target")
            print(matrix[mrow][mcol])
            return self.bs(matrix, 1 + mrow*cols + mcol,end,target)        

    def mapTo(self, index: int, cols: int):
        return (index // cols,index % cols)
    
    def bs2(self,arr,start,end,target):
        middle = (start + end) // 2
        print(arr)
        print(f"Start: {start}, End: {end}")

        if arr[middle] == target:
            return middle
        if arr[end] == target:
            return end
        if arr[start] == target:
            return start      
        if start >= end and arr[middle] != target:
            return -1
        if arr[middle] > target:
            return self.bs2(arr,start,middle - 1,target)
        return self.bs2(arr,middle + 1,end,target)          
    

matrix = [[1], [3]]
target = 0
print(Solution().searchMatrix(matrix,target))
        