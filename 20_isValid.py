class Solution:
	def isValid(self, s: str):
		stack = [None]

		seq = s.replace(' ', '')
		for i in seq:
			if i in '{([':
				stack.append(i)
			elif i == '}' and stack[-1] == '{':
				stack.pop()
			elif i == ')' and stack[-1] == '(':
				stack.pop()
			elif i == ']' and stack[-1] == '[':
				stack.pop()
			else:
				return False

		if stack == [None]:
			return True
		else:
			return False

sol = Solution()
# import pdb; pdb.set_trace()
print(sol.isValid('    ()()[{}(())'))
# print(len('') % 2)