class TimeMap:

    def __init__(self):
        self.d = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.d:
            self.d[key] = [(value, timestamp)]
        else:
            self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.d.get(key, [])
        l = 0
        r = len(vals) - 1
        res = None
        while l <= r:
            m = (l + r) // 2
            t = vals[m][1]
            #print(f"t: {t}")
            if t < timestamp:
                if res != None and t > res[1]:
                    res = vals[m]
                    #print("Res got updated")
                elif res == None:
                    res = vals[m]
                    #print("Res got init")                    
                l = m + 1
            elif t > timestamp:
                r = m - 1
            else:
                #print("Hi")
                res = vals[m]
                break
        if res == None: # all t values are greater than timestamp
            return ""
        return res[0]
        
            


#Your TimeMap object will be instantiated and called as such:

def testTimeMap(functions, params):
    results = []
    timeMap = None
    
    for i, func_name in enumerate(functions):
        if func_name == "TimeMap":
            timeMap = TimeMap()
            results.append(None)
        elif func_name == "set":
            key, value, timestamp = params[i]
            result = timeMap.set(key, value, timestamp)
            results.append(result)
        elif func_name == "get":
            key, timestamp = params[i]
            result = timeMap.get(key, timestamp)
            results.append(result)
    
    return results

functions = ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
params = [[], ["love","high",10], ["love","low",20], ["love",5], ["love",10], ["love",15], ["love",20], ["love",25]]

output = testTimeMap(functions, params)
print(output)



#[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
