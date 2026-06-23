from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif char == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif char in ["(", "{", "["]:
                stack.append(char)
            else :
                return False

        return not stack