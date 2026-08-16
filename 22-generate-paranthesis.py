
def generateParenthesis(n):

    pairs = []
    
    def backtrack(open, close, pair):
        if open == close == n:
            return pair
        if close < open:
            pair =  pair + ")"
            return backtrack(open,close+1,pair)
        if open < n :
            pair = pair + "("
            return backtrack(open + 1,close,pair)
        
#NOPE