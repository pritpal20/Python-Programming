

hacstack = "Pritpal Singh"

needle ="Billu"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needle_len = len(needle)
        haystack_len = len(haystack)

        if needle_len > haystack_len or needle_len == 0:
        	return -1

        j = needle_len
        for i in range(haystack_len):

        	print(haystack[i:j])
        	j+=1

        	sub_str = haystack[i:j-1]
        	print(f"needle = <{needle}> , sub_str = <{sub_str}>")
        	if needle == sub_str:
        		return i


        return -1






S1 = Solution()

print(S1.strStr(hacstack,needle))