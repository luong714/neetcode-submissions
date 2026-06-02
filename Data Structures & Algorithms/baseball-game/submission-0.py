class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for index in operations:
            if index == "+":
                stack.append(stack[-1]+ stack[-2])
            elif index == "D":
                stack.append(stack[-1] * 2)
            elif index == "C":
                stack.pop()
            else:
                stack.append(int(index))
        return sum(stack)