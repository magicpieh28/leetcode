class Solution:
	def lengthOfLastWord(self, s: str):
		self.s = s

		string = s.split(' ')
		space = ''
		
		for idx, i in enumerate(string[::-1]):
			if i == space and idx != len(string) - 1:
				continue
			elif i == space and idx == len(string) - 1:
				print(0)
				return 0
			elif i != space:
				print(len(i))
				return len(i)

sol = Solution()
sol.lengthOfLastWord('         ')
