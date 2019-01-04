class Solution:
	def canConstruct(self, ransomnote, magazine):
		for s in set(ransomnote):
			if ransomnote.count(s) > magazine.count(s):
				return False
		return True


sol = Solution()
ransomnote = "fffbfg"
magazine = "effjfggbffjdgbjjhhdegh"
print(sol.canConstruct(ransomnote, magazine))