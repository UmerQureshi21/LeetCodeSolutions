class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            for i in range(3,numRows+1):
                row = []
                for j in range(i):
                    if j == 0 or j == i - 1:
                        row.append(1)
                    else:
                        row.append(rows[i-2][j-1] + rows[i-2][j])
                rows.append(row)
        return rows
        

#3ms Beats 18.89%