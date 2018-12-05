class Solution:
	def isValid(self, s: str):
		self.s = s
		s = s.replace(" ", "")
		s = list(s)

		open_, close_ = '{([',  '})]'

		bools = []
		indice = 0

		while s:
			if len(s) >= 2 and indice != len(s) - 1 and indice < len(s) - 1:
				if s[indice] in open_:
					if s[indice + 1] in open_:
						if indice + 1 == len(s) - 1:
							return False
						else:
							indice += 1
					elif s[indice + 1] in close_:
						if s[indice + 1] == close_[open_.index(s[indice])]:
							del s[indice]; del s[indice]
							bools.append(True)
						else:
							return False
				elif s[indice] in close_:
					if indice >= 1:
						indice -= 1
					elif indice == 0:
						return False
				else:
					return False

			elif s and indice == len(s) - 1:
				indice -= 1

			elif len(s) == 0 and bools:
				return False

			elif indice > len(s) - 1:
				indice -= 1

			else:
				return False

		if len(s) == 0 and True in bools:
			return True

		elif len(s) == 0 and not bools:
			return True

		else:
			return False
