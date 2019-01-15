class Solution:
	def romanToInt(self, s: str):
		values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
		s = [values[x] for x in s]
		# + [0]을 하는 이유는 비교하려는 대상의 길이를 맞추기 위해
		return sum(-x if x < y else x for x, y in zip(s, s[1:] + [0]))

sol = Solution()
# import pdb; pdb.set_trace()
print(sol.romanToInt('MDIV'))