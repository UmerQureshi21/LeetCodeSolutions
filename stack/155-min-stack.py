class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.mins = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size+=1
        if(self.size == 1 or val < self.mins[len(self.mins) - 1]["val"]):
            self.mins.append(self.PM(val,self.size - 1))


    def pop(self) -> None:
        self.stack.pop()
        self.size -=1
        if(self.mins[len(self.mins) - 1]["index"] == self.size):
            self.mins.pop()
        
            
    def top(self) -> int:
        return self.stack[self.size - 1]
        

    def getMin(self) -> int:
        return self.mins[len(self.mins) - 1]["val"]
        
        
    @staticmethod #prevnets you from having to pass in self
    def PM(val: int,index: int) -> dict:
        return {
            "val":val,
            "index":index
        }

 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()