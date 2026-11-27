class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        #s = aaabbcccaaa => [{letter: a, start: 0, count: 3}, {letter: b, start: 3, count: 2}, {letter: c, start: 5, count: 3}, {letter: a, start: 8, count: 3}]
        counts = []
        curr = s[0]
        start = 0
        count = 1
        for i, letter in enumerate(s[1:]):
            if letter == curr:
                count += 1
            else:
                counts.append(self.make(curr,start, count))
                start = i + 1
                count = 1
                curr = letter
        counts.append(self.make(curr,start, count))

        l = len(counts)
        totals = []
        for i in range(l):
            total = {}
            for j in range(i, l):
                c = counts[j]
                if not c["letter"] in total:
                    total[c["letter"]] = c["count"]
                else:
                    total[c["letter"]] = total[c["letter"]] + c["count"]
                # print(f"{i}: {total}")
                sum = 0
                allk = True
                for letter in total:
                    if total[letter] < k:
                        allk = False
                    else: 
                        sum += total[letter]
                totals.append(sum) if allk else None
        return self.findMax(totals)
    def make(self, letter, start, count):
        return {"letter": letter, "start": start, "count": count}
    def findMax(self, totals):
        max = 0
        for num in totals:
            if num > max:
                max = num
        return max
    

sol = Solution()
s = "aaabbbcbbbaaaa"
k = 3
print(sol.longestSubstring(s,k))

