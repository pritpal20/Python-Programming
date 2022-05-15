class Solution(object):
    def isValid(self, s):
        
        stack = ['N']
        m = {')':'(',']':'[','}':'{'}
        # print("m.keys - ",m.keys())
        for i in s:
            if i in m.keys():
                if stack.pop() != m[i]:
                    return False
            else:
                stack.append(i)
                
        return len(stack) == 1



Sol = Solution()

print(Sol.isValid(")("))