
def sumAllPairDifferences(L: list[int]):
    L.sort()
    prefixSums = [0] * len(L)
    sum = 0
    for i, num in enumerate(L):
        sum = sum + num
        prefixSums[i] = sum
    
    diffs = [0] * len(L)

    for i,num in enumerate(L):
        if i == 0:
            diffs[i] = 0
        else:            
            diffs[i] = num * i - prefixSums[i-1]

    s = 0
    for num in diffs:
        s += num
    
    return s
        



    #for a fixed i, the value will be L[i] * i - (L[0] + L[1] + ... + L[i-1])


def sumAllPairDifferencesBetter(L: list[int]) -> int:
    L.sort()
    prefix = 0
    ans = 0
    for i, x in enumerate(L):
        ans += x * i - prefix   # x - all previous
        prefix += x
    return ans



print(sumAllPairDifferencesBetter([2,23,32,23]))
