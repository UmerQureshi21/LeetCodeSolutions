class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2) < len(s1)):
            return False
        matches = 0
        s1d = {}
        alph = "abcdefghijklmnopqrstuvwxyz"
        for letter in alph:
            s1d[letter] = 0
        for letter in s1:
            s1d[letter] = s1d[letter] + 1
        s2d = {}
        for letter in alph:
            s2d[letter] = 0
        for letter in s2[0:len(s1)]:
            s2d[letter] = s2d[letter] + 1
        for key in s1d:
            if s1d[key] == s2d[key]:
                matches += 1
        if len(s1) == len(s2) and matches != 26:
            return False
        lp = 1
        rp = len(s1) + 1
        while not (matches == 26 or rp > len(s2)):
            removed = s2[lp-1]
            s2d[removed] = s2d[removed] - 1
            if s2d[removed] == s1d[removed]: 
                matches += 1
            elif s2d[removed] + 1 == s1d[removed] and s2d[removed] != s1d[removed]: 
                matches -= 1
            added = s2[rp-1]
            s2d[added] = s2d[added] + 1
            if s2d[added] == s1d[added]:
                matches += 1
            elif s2d[added] - 1 == s1d[added] and s2d[added] != s1d[added]:
                matches -= 1      
            lp += 1
            rp +=1
        return matches == 26       
            
            
                
        
            

        
        
    
    
    
if __name__ == "__main__":
    print(Solution().checkInclusion("abc","akdfuewidjskfmcldjdbaclsljfh"))