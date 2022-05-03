

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:


        j = len(nums)
        print(" j =",j)
        for i in range(len(nums)):
            
            if nums[i] == val:
                print("index ",i)
                self.delete(nums[i:],0)


        print("nums after remove = " ,nums)
        return nums



    def delete(self,l1,index):

        len_l1 = len(l1)
        if index < len_l1 -1:
            self.shift_items(l1,index,len_l1)

        del l1[len_l1-1]

        return l1

    def shift_items(self,l1,index,len_l1):

        for i in range(index,len_l1-1):
            l1[i] = l1[i+1]

        print("l1 = ",l1)

        # return l1
        




S1 = Solution()

l1 = [0,1,2,3,2,4,5,2]

print(l1)
l1 = S1.removeElement(l1,1)

print(l1)