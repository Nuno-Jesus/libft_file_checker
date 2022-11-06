class ProjectFile:
	def __init__(self, func, header, allowed_funcs):
		self.func = func
		self.header = header
		self.allowed_funcs = allowed_funcs
		self.wasDelivered = False

	def check_header(self):
		if self.func.startswith('ft_lst'):
			f = open(self.func + '_bonus.c', 'r')
		else:
			f = open(self.func + '.c', 'r')

		line = f.readline()
		while line != '':
			if line.find(self.header) != -1:
				f.close()
				return ''

			line = f.readline()
		f.close()
		return self.func