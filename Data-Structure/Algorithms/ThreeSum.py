#   

class Solution:
    def threeSumClosest(self, nums: list(), target: int) -> int:

        if len(nums) < 3 :
            return 0

        nums_sum = 0
        r = 0 
        d = 0

        print("given list --> ",nums)
        print("Given target --> ",target)
        for idx,item in enumerate(nums):
            print(f"**idx ={idx} , item = {item}")
            print(f"**target = {target} , r = {r}, nums_sum = {nums_sum}")

            close_num = target - nums_sum
            if target - nums_sum 


        print(f"nums_sum = {nums_sum} ,r = {int(r)} , d = {d}")

        exit(0)
        return int(d)


# A = [-1,2,1,-4]
A = [1,2,3,1]
Soln = Solution()

print("three sum closes = ",Soln.threeSumClosest(A,1))


        