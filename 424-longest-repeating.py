class Solution:
    def mySol(self, s: str, k: int) -> int:
        if k == 0:
            return 1
        
        maxCount = 0
        letters = {}
        maxConsecCount = 1
        maxConsec = s[0]
        for i,char in enumerate(s):
            if not char in letters:
                letters[char] = 1
            count = 1
            j = i + 1
            while j < len(s):
                if s[j] == char:
                    count += 1
                else:
                    break
                j += 1
            if count > letters[char]:
                letters[char] = count

        for letter in letters:
            if letters[letter] > maxConsecCount:
                maxConsecCount = letters[letter]
                maxConsec = letter
        
        lp = 0
        rp = 0
        maxCount = 1
        if k == 1:
            while rp < len(s):
                c = s[rp]
                if c != maxConsec:
                    if k > 0:
                        k -= 1
                    if k == 0:
                        count = 1# add to this any letters after that are maxConsec
                        i = rp + 1
                        while i < len(s):
                            if s[i] == maxConsec:
                                count += 1
                            else:
                                break
                            i += 1
                        
                        i = rp - 1
                        while i >= 0:
                            if s[i] == maxConsec:
                                count += 1
                            else:
                                break
                            i -= 1
                        if count > maxCount:
                            maxCount = count
                rp += 1
        else:
            while rp < len(s):
                c = s[rp]
                if c != maxConsec:
                    if k > 0:
                        k -= 1
                    if k == 0:
                        count = rp - lp + 1# add to this any letters after that are maxConsec
                        i = rp + 1
                        while i < len(s):
                            if s[i] == maxConsec:
                                count += 1
                            else:
                                break
                            i += 1
                        
                        i = lp - 1
                        while i >= 0:
                            if s[i] == maxConsec:
                                count += 1
                            else:
                                break
                            i -= 1
                        if count > maxCount:
                            maxCount = count
                        lp = rp # lp now points to first letter to replace
                rp += 1

            count = rp - lp # add to this any letters after that are maxConsec
            i = rp + 1
            while i < len(s):
                if s[i] == maxConsec:
                    count += 1
                else:
                    break
                i += 1
            
            i = lp - 1
            while i >= 0:
                if s[i] == maxConsec:
                    count += 1
                else:
                    break
                i -= 1
            if count > maxCount:
                maxCount = count


        return maxCount
    
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 0

        lp = 0
        rp = 0
        mostFreq = 0
        while rp < len(s):
            counts[s[rp]] = counts[s[rp]] + 1
            # mostFreq = self.mostFreq(counts)
            mostFreq = max(mostFreq, counts[s[rp]])
            window = rp - lp + 1
            if window - mostFreq <= k and window > maxLen:
                maxLen = window
            elif window - mostFreq > k: 
                valid = False
                while not (valid or lp == rp):
                    counts[s[lp]] = counts[s[lp]] - 1
                    lp += 1
                   # mostFreq = self.mostFreq(counts)
                    window = rp - lp + 1
                    if window - mostFreq <= k:
                        valid = True
                    if window > maxLen:
                        maxLen = window
            rp += 1

        return maxLen
    
    def mostFreq(self,counts):
        maxCount = 0
        for letter in counts:
            if counts[letter] > maxCount:
                maxCount = counts[letter]
        return maxCount
        
s = "AABABBBA"
k = 23453

s = "ABABBBAA"
k = 3

s = "ABAB"
k = 3


print(Solution().characterReplacement(s, k))