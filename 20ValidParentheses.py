#works,  ~77% runtime, ~25% memory
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ind = -1
        for x in s:
            if x == "(" or x == "[" or x == "{":
                stack.append(x)
                ind+=1
            elif not stack: #stack empty, other brackets wont work
                return False
            elif (x == ")" and stack[ind] == "(") or (x == "}" and stack[ind] == "{") or (x == "]" and stack[ind] == "[")  :
                stack.pop()
                ind-=1
            else: #no other combo is valid
                return False
        if not stack: #stack is empty at the end
            return True
        else:
            return False
