class Solution(object):
	def countAndSay(self, n: int):
		self.n = n

		outputs = {}

		loop_count = 1

		# import pdb; pdb.set_trace()

		while loop_count <= 30:
			if loop_count == 1:
				outputs[loop_count] = str(loop_count)
				loop_count += 1
				# print(f'outputs => {outputs}')

			elif len(outputs[loop_count - 1]) == 1:
				num = outputs[loop_count - 1].count(outputs[loop_count - 1])
				num = str(num) + outputs[loop_count - 1]
				outputs[loop_count] = num
				loop_count += 1
				# print(f'outputs => {outputs}')

			else:
				number = []
				count = 0
				for idx, i in enumerate(outputs[loop_count - 1]):
					if idx != len(outputs[loop_count - 1]) - 1:
						if outputs[loop_count - 1][idx] == outputs[loop_count - 1][idx + 1]:
							if (idx+1) == len(outputs[loop_count -1]) -1:
								count += 1
								num = str(count + 1) + i
								number.append(num)
							elif (idx + 1) != len(outputs[loop_count - 1]) -1:
								count += 1
						elif outputs[loop_count - 1][idx] != outputs[loop_count - 1][idx + 1]:
							if (idx + 1) == len(outputs[loop_count - 1]) -1:
								num = str(count + 1) + i
								number.append(num)
								count -= count

								num = str(1) + outputs[loop_count - 1][idx + 1]
								number.append(num)

							elif (idx + 1) != len(outputs[loop_count - 1]) -1:
								num = str(count + 1) + i
								number.append(num)
								count -= count

				num = ''.join(number)
				outputs[loop_count] = num
				loop_count += 1
				# print(f'outputs => {outputs}')
				del number[:]
				# import pdb; pdb.set_trace()

		return outputs[n]
