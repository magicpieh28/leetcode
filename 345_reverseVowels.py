class Solution:
	def reverseVowels(self, string):
		vowels = 'aeiouAEIOU'

		vow = []
		for s in string:
			if s in vowels:
				vow.append(s)

		if not vow:
			return string

		sttr = list(string)
		for idx, s in enumerate(sttr):
			if s in vowels:
				sttr[idx] = vow[-1]
				vow.pop()

		return ''.join(sttr)


sol = Solution()
string = "aA"
print(sol.reverseVowels(string))