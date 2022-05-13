class Solution:
    def plusOne(self, digits: list()) -> list():
        
        
        j = len(digits)
       
        for i in range(j):

            if digits[j-i-1] == 9 :
                digits[j-i-1] = 0
            else:
                digits[j-i-1] += 1
                break


        if digits[0] == 0 :
            digits[0] = 1
            digits.append(0)

            
                      
            
                
                
                
        return digits


Soln = Solution()
print(Soln.plusOne([1,9,9,9,9]))