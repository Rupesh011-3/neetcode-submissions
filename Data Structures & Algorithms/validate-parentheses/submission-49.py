class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = {"}":"{","]":"[",")":"("}

        for i in s:
            if i in o:
                if stack and stack[-1]==o[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        