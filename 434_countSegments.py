class Solution:
	def countSegments(self, s: str):
		return len(s.split())

sol = Solution()
string = "Hello, my name is John"
print(sol.countSegments(string))