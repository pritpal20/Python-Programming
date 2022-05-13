class Solution:
    def plusOne(self, digits: list()) -> list():
        
        
        j = len(digits)
        ret_digit = []
        for i in range(j):
            
            print(digits[j-i-1])
            
            if digits[j-i-1] < 9:
                digits[j-i-1] = digits[j-i-1] + 1
                return digits
            else:
                print('here i ',i,' j ',j -1)
                print("->",digits)
                if digits[j-i-1] == 9 and i == j - 1:
                    # ret_digit = digits
                    ret_digit.append(1)
                    ret_digit.append(0)
                    print(' ret_digit',ret_digit)
                    print(' digits[1:]',digits[1:])
                    ret_digit = ret_digit + digits[1:]
                else:
                    digits[j-i-1] = 0
                    # return digits
                
                
                
        return ret_digit


Soln = Solution()
print(Soln.plusOne([9,9,9]))