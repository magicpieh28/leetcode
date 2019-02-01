class Solution:
	def detectCapitalUse(self, s: str):
		if s.isupper():
			return True
		if len(s) > 1:
			if s.islower() or s.islower():
				return True
			if s[0].isupper() and s[1:].islower():
				return True
		if len(s) == 1 and s.islower():
			return True
		else:
			return False

sol = Solution()
string = "gggg"
print(sol.detectCapitalUse(string))