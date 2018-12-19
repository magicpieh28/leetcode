class Solution:
	def longestCommonPrefix(self, strings: list):
		prefix = [[] for _ in range(len(strings))]

		# import pdb; pdb.set_trace()
		if not strings:
			return ''
		else:
			minString = min(strings, key=len)

			i = 0
			for idx, string in enumerate(strings):
				while i <= len(minString)-1:
					if minString[i] == string[i]:
						prefix[idx].append(minString[i])
						i += 1
					else:
						break
				i = 0

		char = [c[0] for c in zip(*prefix)]
		return ''.join(char)


sol = Solution()
strings = ["dog", "cat"]
print(sol.longestCommonPrefix(strings))