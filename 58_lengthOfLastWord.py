class Solution:
	def lengthOfLastWord(self, s: str):
		self.s = s

		inverse_s = s[::-1]
		space = ' '
		count = 0
		for idx, string in enumerate(inverse_s):
			if len(inverse_s) != 1 and idx != (len(inverse_s) - 1):
				if string == space and inverse_s[idx+1] != space:
					count += 1
				elif string == space and inverse_s[idx+1] == space:
					count += 0
				elif string != space and inverse_s[idx+1] != space:
					count += 1
				elif string != space and inverse_s[idx+1] == space:
					if idx == 0:
						count += 1
						break
					elif (idx + 1) != len(inverse_s) - 1 and inverse_s[0] != space:
						count += 1
						break
					elif (idx + 1) != len(inverse_s) - 1 and inverse_s[0] == space:
						break
					elif (idx + 1) == len(inverse_s) - 1 and inverse_s[0] != space:
						count += 1
						break
			elif len(inverse_s) == 1 and idx == (len(inverse_s) - 1):
				if string == space:
					break
				elif string != space:
					count += 1
			elif len(inverse_s) != 1 and idx == (len(inverse_s) - 1):
				if inverse_s[0] == space:
					break
				count += 1
		print(count)
		return count


sol = Solution()
sol.lengthOfLastWord(' abcs')