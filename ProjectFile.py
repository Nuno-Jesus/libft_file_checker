class ProjectFile:
	def __init__(self, func, header, allowed_funcs):
		self.func = func
		self.header = header
		self.allowed_funcs = allowed_funcs
		self.wasDelivered = False

	def __eq__(self, other):
		return self.func 

	def check_header(self):
		f = open(self.func + '\n', 'r')

		line = f.readline()
		while line != '':
			if line.find(self.func + '(') != -1:
				if line != self.header + '\n':
					return {self.func, [self.header, line]}
				
				f.close()
				return {}

			line = f.readline()

		return {self.func, [self.header, None]}