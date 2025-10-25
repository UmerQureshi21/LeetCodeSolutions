class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        letterCoords = [[s[0],[0,0]]]
        row = 0
        col = 0
        startIncrementing = True
        for letter in s[1:]:
            if row + 1 < numRows and startIncrementing:
                row+=1
            elif row >= 0:
                if row == 0:
                    startIncrementing = True
                    row +=1
                else:
                    startIncrementing = False 
                    row -=1
                    col+=1
            letterCoords.append([letter,[row,col]])    
        segmentsByRowNum = {}
        for lc in letterCoords:
            if lc[1][0] in segmentsByRowNum:
                segmentsByRowNum[lc[1][0]] += lc[0]
            else:
                segmentsByRowNum[lc[1][0]] = lc[0]
        word = ""
        for key in segmentsByRowNum:
            word+=segmentsByRowNum[key]
        
        return word
        