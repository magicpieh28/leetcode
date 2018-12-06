class Solution:
	def isPalindrome(self, s):
		self.s = s

		s = [i.lower() for i in s if i.isalnum()]
		bools = []
		if not s:
			return True
		else:
			for (i, j) in zip(s, s[::-1]):
				if i == j:
					bools.append(True)
				else:
					return False

		if bools:
			return True

is_pal = "A man, a plan, a canal: Panama"
not_pal = "race a car"

sol = Solution()
sol.isPalindrome(not_pal)