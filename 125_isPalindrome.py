import re


class Solution:
	def isPalindrome(self, s):
		self.s = s

		pattern = re.compile(r"[a-zA-Z]")
		input_s = [c.lower() for c in s if pattern.match(c)]
		inverse_s = input_s[::-1]
		bools = []
		for (i, j) in zip(input_s, inverse_s):
			if i == j:
				bools.append(True)
			else:
				bools.append(False)

		if False in bools:
			return False
		elif True in bools:
			return True
		elif not bools:
			return True

is_pal = "A man, a plan, a canal: Panama"
not_pal = "race a car"

sol = Solution()
sol.isPalindrome("OP")