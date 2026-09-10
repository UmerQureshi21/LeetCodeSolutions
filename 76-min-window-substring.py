from collections import defaultdict
from typing import Dict, List

class Attempt:
    def minWindow(self, s: str, t: str) -> str:
        t_hash = self.toHashMap(t)
        min_win = ""
        char_map: Dict[str, List[int]] = {}
        start = 0
        remaining_chars = len(t)
        
        if len(t) > len(s):
            return ""

        for i, char in enumerate(s):
            if char in t_hash and t_hash[char] == "not encountered":
                t_hash[char] = "encountered"
                if remaining_chars == len(t): #first char encountered, start minwin from here
                    start = i
                remaining_chars -= 1
                if remaining_chars == 0:
                    min_win = s[start:(i + 1)]
                    print(f"first min win: {min_win}")

                char_map[char] = [i]
            elif char in t_hash and min_win != "" and t_hash[char] == "encountered":
                print(f"{char} is seen on index {i}")
                char_map[char].append(i)
                chars_needed = 0
                first_index = len(s) # arbitraty big value
                for tchar in char_map:
                    if char != tchar:
                        idx = self.biggestIdxBetween(char_map[tchar], start, i)
                        if idx < first_index:
                            first_index = idx
                if (i - first_index) <= len(min_win):
                    min_win = s[first_index: (i+1)]
                    start = first_index
                else:
                    print(f"not smaller, {s[first_index: (i+1)]}")                
                #now we do the char hash checkk
        print(char_map)



        return min_win

    def toHashMap(self, t: str):
        hashmap = defaultdict(lambda: "default_value")
        for char in t:
                hashmap[char] = "f{}"
        print(dict(hashmap))
        return dict(hashmap)
    
    # i think that we can honestly just return last element of list since that value implies below
    def biggestIdxBetween(self, L: List[int], lower: int, higher: int):
        biggest = L[0]
        for num in L[1:]:
            if num >= lower and num <= higher and num > biggest:
                biggest = num
        return biggest


class AttemptTwo:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) == 1:
            for char in s:
                if char == t:
                    return t
                
            return ""
        
        T = {}
        for char in t:
            if not char in T:
                T[char] = 1
            else:
                T[char] = T[char] + 1
        window = {}
        for char in t:
            if not char in window:
                window[char] = 0
        print(f"T: {T},\nWindow: {window} \n")
        
        minwin = ""
        lp = 0
        rp = 0
        
        for char in s:
            if s[rp] in T and minwin == "":
                if window[s[rp]] < T[s[rp]]:
                    window[s[rp]] += 1 
                if self.firstMinWin(window, len(t)):
                    while self.firstMinWin(window, len(t)):
                        if s[lp] in T:
                            window[s[lp]] -=1
                        lp +=1
                    lp -= 1
                    minwin = s[lp:(rp+1)]
                    print(f"minwin found, {minwin}")
                window[s[rp]] = window[s[rp]] + 1
            elif s[rp] in T and minwin != "":
                window[s[rp]] = window[s[rp]] + 1
                temp = window.copy()
                print(temp)
                while not s[lp] in T or temp[s[lp]] > T[s[lp]]:
                    if s[lp] in T and s[lp] in temp:
                        temp[s[lp]] = temp[s[lp]] - 1
                    lp += 1
                if rp - lp  < len(minwin):
                    minwin = s[(lp):(rp+1)]
                    window = temp
                    print(f"minwin update, {minwin}")
                
            rp+=1

        return minwin
    
    def firstMinWin(self, first_min_win: Dict[str, int], Tlen: int):
        count = 0
        for char in first_min_win:
            count += first_min_win[char]
        return count == Tlen
            

class AttemptThree:
    def minWindow(self, s: str, t: str) -> str:
        T = {}
        window = {}
        for char in t:
            window[char] = 0
            if not char in T:
                T[char] = 1
            else:
                T[char] = T[char] + 1
        conditionsNeeded = len(list(T.keys()))
        conditionsMet = 0
        
        lp = 0
        rp = 0
        minwin = ""
        
        for char in s:
            if char in window:
                window[char] = window[char] + 1
                if window[char] == T[char]:
                    conditionsMet += 1
                if conditionsMet == conditionsNeeded:
                    win = s[lp: (rp+1)]
                    if (minwin != "" and len(win) < len(minwin)) or minwin == "":
                        minwin = win
                    print(f"window before shrinking: {window}")
                    while conditionsMet == conditionsNeeded:
                        if s[lp] in window:
                            window[s[lp]] = window[s[lp]] - 1
                            if window[s[lp]] < T[s[lp]]:
                                conditionsMet -= 1
                            else:
                                lp += 1
                        else:
                            lp += 1
                                # print(f"lp: {lp}, rp: {rp}")
                        
                    print(f"lp: {lp}, rp: {rp}, word: {s[lp: (rp+1)]}")
                    print(f"window after shrinking: {window}\n")
                        
            rp+=1
        return minwin
        

class NeetCodeSolution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t

        countT, window = {}, {}
        
        for c in t:
            countT[c] = 1 + countT.get(c,0)
            
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        # r is the right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update our result
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)
                #pop from left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                    
        l, r = res
        return s[l: (r+1)] if resLen != float("infinity") else ""
                
                
s = "ADOBECODEBANC"
t = "ABC"

# s = 'bba'
# t = 'ba'

print(NeetCodeSolution().minWindow(s,t))