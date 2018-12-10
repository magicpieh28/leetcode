class Solution:
	def romanToInt(self, s: str):
		self.s = s

		roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
		number = [1000, 500, 100, 50, 10, 5, 1]

		result = 0
		index = 0
		try:
			while index <= len(s) - 1:
				print(s[index])
				print(index)
				if index == len(s) - 1:
					result += number [roman.index(s[index])]
					break
				elif number[roman.index(s[index])] < number[roman.index(s[index + 1])]:
					num = number[roman.index(s[index + 1])] - number[roman.index(s[index])]
					result += num
					index += 2
				else:
					result += number[roman.index(s[index])]
					index += 1
		except ValueError:
			result = 0

		return result

sol = Solution()
# import pdb; pdb.set_trace()
print(sol.romanToInt(' '))