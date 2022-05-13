

class Solution:

    def middle(self, left , right):

        print(f'left-> {left} ,right->{right}')

        return int( left + (right - left ) / 2 )



    def search(self, nums: list(), target: int) -> int:
        
        len_nums = len(nums)      

        left = 0 
        right = len_nums -1 
        mid = self.middle(left,right)
        while(left <= right ):

            print(f'left {left} , right {right} ,middle = ',mid)

            if target == nums[mid]:
                print('Match found at ',mid)
                return mid 
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = self.middle(left,right)

        print('Match not found')

        return -1



A = [-1,0,3,4,5,7,9,10,100]



Soln = Solution()

print(Soln.search(A,200))




