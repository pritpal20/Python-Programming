class Solution:
    def reverse(self, x: int) -> int:

        mul = 1
        if x < 0 :
            mul = -1
            x = abs(x)
            return False
        rev = 0
        while x != 0 :

            pop = x % 10
            print("pop",pop)

            rev = rev* 10 + pop
            print("rev",rev)

            x = x // 10

        print(rev)

        if rev < pow(-2,31) or rev > pow(2,31) - 1:
            return 0

        return mul * rev

    def isPalindrome(self, x: int) -> bool: 

        if self.reverse(x) == x :
            return True
        else:
            return False


Soln = Solution()

print(Soln.reverse(-123))

print(Soln.isPalindrome(101))