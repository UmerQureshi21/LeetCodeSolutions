from typing import List

    #so if its anumber then push onto stack
    #if its an operand, then pop the two numbers, do the operation, and push the result onto the stack
        
def evalRPN( tokens: List[str]) -> int:
    stack: List[int] = []
    for token in tokens:
        if token in ['+','*','/','-']:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            print("operator ",num1, token ,num2)
            if token == '+':
                stack.append(num1 + num2)
            if token == '-':
                stack.append(num1 - num2)
            if token == '*':
                stack.append(num1 * num2)
            else:
                stack.append(num1 / num2)
        else:
            print("operand ", token)
            stack.append(int(token))
        print(stack)

    return stack[-1]
    
    
print(evalRPN(["2","1","+","3","*"]))
            