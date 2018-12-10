class Solution:
	def lengthOfLastWord(self, s: str):
		self.s = s

		string = s.split()
		try:
			return len(string[-1]) if string[-1].isalpha() else 0
		except IndexError:
			return 0

sol = Solution()
print(sol.lengthOfLastWord('         '))
