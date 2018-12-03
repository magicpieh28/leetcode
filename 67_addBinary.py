class Solution:
	def addBinary(self, a, b):
		self.a = a
		self.b = b

		try:
			result = int(a, 2) + int(b, 2)
			return str(bin(result)[2:])
		except SyntaxError:
			return None

sol = Solution()
sol.addBinary('11', '1')