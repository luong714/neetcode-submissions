class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeAndopen = {")" : "(" , "}" : "{" , "]" : "["}
        for char in s:
            if char in closeAndopen:
                if stack and stack[-1] == closeAndopen[char]:
                    stack.pop()
                else: return False
            else:
                stack.append(char)
        return len(stack) == 0