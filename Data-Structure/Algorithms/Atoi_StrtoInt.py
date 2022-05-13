

class Solution:
    def myAtoi(self, s: str) -> int:

        num = 0
        mul = 1
        for letter in s:

            if letter not in ['1','2','3','4','5','6','7','8','9','0'] :
                if letter == "-":
                    mul = -1
                continue

            num = num * 10 + int(letter)

        return mul * num




Soln = Solution()

print(Soln.myAtoi("words and 987"))


