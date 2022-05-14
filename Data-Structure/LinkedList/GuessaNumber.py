class Solution:

    def guess(self,n: int)->int :

        print("num  = ",n)
        guess_num = 51 
        if n == guess_num :
            return 0
        elif n > guess_num :
            return -1
        else:
            return 1


    def guessNumber(self, n: int) -> int:
        
        left = 0
        right = n 
        
        i = 0
        while(left <= right):
            
            mid = int ( (right + left) / 2 )

            print(f"left = {left}, right = {right} ,mid = {mid}")

            # if mid is less than num
            if self.guess(mid) == 1 :
                left = mid + 1
               
            elif self.guess(mid) == -1:
                right = mid - 1
            else:
                return mid

            i+=1
            if i > 10 :
                break



Soln = Solution()


print(Soln.guessNumber(100))