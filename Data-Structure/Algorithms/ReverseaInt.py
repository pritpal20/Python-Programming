class Solution:
    def reverse(self, x: int) -> int:
        # print(x)

        mul = 0
        if x  < 0 :
            mul = -1
        else:
            mul = 1
        x = abs(x)
        i = 1 
        num = 0
        l1 = []
        j = 0 
        while(x > 0 ):
            
            # print("Remainder ",x % 10)
            l1.append(x % 10 )
            x = x // 10
            j += 1 



        # print(l1)
        # print(j-1)

        # mul = 1
        num = 0
        for i in range(j):
            # print("index ",j-i-1)
            num += mul * l1[j-i-1]
            mul = mul* 10


        if num < pow(-2,31) or num > pow(2,31) - 1:
            return 0

        print(num)




S1 = Solution()
S1.reverse(1534236469)


# print(123 // 10)