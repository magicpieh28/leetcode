class Solution:
	def strStr(self, haystack, needle):
		if haystack == needle:
			return 0
		if len(needle) == 0:
			return 0
		if needle in haystack:
			for i in range(len(haystack)):
				if haystack[i:i+len(needle)] == needle:
					return i
		else:
			return -1


sol = Solution()
haystack = "a"
needle = "a"
print(sol.strStr(haystack, needle))