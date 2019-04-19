class Solution:
	def findLUSlength(self, a: str, b: str):
		if a == b:
			return -1
		else:
			return max(len(a), len(b))


sol = Solution()
print(sol.findLUSlength('aba', 'aba'))