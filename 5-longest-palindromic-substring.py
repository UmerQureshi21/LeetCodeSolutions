def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s
    elif len(s) == 2:
        if s[0] == s[1]:
            return s
        return s[0]
    
    lp = 0
    rp = 2
    pal = s[0]
    
    while rp < len(s):
        if s[lp] == s[lp+1] and s[lp] != s[rp] and lp == 0:
            pal = s[lp:rp]
        elif s[rp-1] == s[rp] and s[lp] != s[rp] and rp == len(s) -1:
            if len(pal) <= 2:
                pal = s[lp+1:]                
        elif s[lp] == s[rp] and lp == 0:
            pal = s[lp:rp+1]
        elif s[lp] == s[rp] and rp == len(s) - 1:
            if len(pal) <= 3:
                pal = s[lp:rp+1]
        if s[lp] == s[rp]:
            l = lp - 1
            r = rp + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if r - l + 1 > len(pal):
                pal = s[l:r+1]
        if s[rp] == s[rp-1]:
            l = lp+1
            r = rp
            while l >=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if r - l + 1 > len(pal):
                pal = s[l:r+1]            
        lp+=1
        rp+=1
    return pal

print(longestPalindrome("s;ldkjra;kracemalkjracecaralskdja; irgu;jnk"))