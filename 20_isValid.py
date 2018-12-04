class Solution:
	def isValid(self, s: str):
		self.s = s
		s = s.replace(" ", "")
		s = list(s)

		open_ = '{(['
		close_ = '})]'

		bools = []
		indice = 0
		while s:
			print(s)
			if len(s) >= 2 and indice != len(s) - 1:
				if s[indice] in open_:
					if s[indice + 1] in open_:
						if s[len(s) - 1] == close_[open_.index(s[indice])]:
							del s[0]; del s[len(s) - 1]
							bools.append(True)
						elif s[len(s) - 1] != close_[open_.index(s[indice])]:
							indice += 1
					elif s[indice + 1] in close_:
						if s[indice + 1] == close_[open_.index(s[indice])]:
							del s[indice]; del s[indice]
							bools.append(True)
						else:
							return False
				elif s[indice] in close_:
					indice -= 1
				else:
					return False
			elif s and indice == len(s) - 1:
				return False
			elif len(s) == 0 and bools:
				return True
			else:
				return False
		if len(s) == 0 and bools:
			return True


s = '{ } ( [ { } { } ] [ ] ) [ { } ]'
print(s)
sol = Solution()
sol.isValid(s)
