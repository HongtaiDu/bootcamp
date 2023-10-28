class Solution:
 def using_stack(self, S):
        stack = []
        for ch in S:
            if ch == '(':
                stack.append(ch)
            else:
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)