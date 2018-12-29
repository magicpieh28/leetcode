class Solution:
	def reverseString(self, s):
		return s[::-1]


sol = Solution()
string = "A man, a plan, a canal: Panama"
print(sol.reverseString(string))