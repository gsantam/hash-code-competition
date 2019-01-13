class OutputExporter():

	def __init__(self, solution, path_output):
		self.path_output = path_output
		self.solution = solution

	def export(self):
		with open(self.path_output, 'w') as file:
			file.write(str(len(self.solution.keys()))+'\n')
			for k, v in self.solution.items():
				file.write("{} {}\n".format(k, ' '.join(map(str, v))))
