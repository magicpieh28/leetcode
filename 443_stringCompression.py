class Solution:
	def compress(self, chars: list):
		result = [chars[0]]
		j = 1
		for i, c in enumerate(chars[1:]):
			if i == len(chars)-2:
				if j+1 > 1:
					for n in str(j+1):
						result.append(n)
			elif c == result[-1]:
				j += 1
			elif c != result[-1]:
				if j > 1:
					for n in str(j+1):
						result.append(n)
				j = 1
				result.append(c)
		return result


sol = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(sol.compress(chars))