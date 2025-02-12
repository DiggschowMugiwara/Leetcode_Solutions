class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack = []
        check = list(part)
        print(check)
        for c in s:
            # print(stack)
            if len(stack) >= len(check) and stack[-len(check):] == check:
                for _ in range(len(check)):
                    stack.pop()
            stack.append(c)
        # print(stack)
        if len(stack) >= len(check) and stack[-len(check):] == check:
            # print("hii")
            for _ in range(len(check)):
                stack.pop()
        return "".join(stack)
