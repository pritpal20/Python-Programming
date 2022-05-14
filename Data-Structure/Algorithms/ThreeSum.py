# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: list(), target: int) -> int:

        if len(nums) < 3 :
            return 0

        nums_sum = 0
        r = 0 
        d = 0 
        for idx,item in enumerate(nums):
            print(f"idx ={idx} , item = {item}")
            print(f"target = {target} , r = {r}, nums_sum = {nums_sum}")
            
            if idx < 3 :
                nums_sum+=item
                continue
                
                if nums_sum != 0:
                    r = target / nums_sum

            if nums_sum != 0:
                d = (target / nums_sum)

            if d < r :
                r = d
            else:
                nums_sum -=item


        print(f"nums_sum = {nums_sum} ,r = {int(r)} , d = {d}")

        return int(d)


A = [-1,2,1,-4]
A = [0,0,0]
Soln = Solution()

print("three sum closes = ",Soln.threeSumClosest(A,1))


        