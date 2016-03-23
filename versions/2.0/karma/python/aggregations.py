class concat:
	def __init__(self, columnName, separator):
		self.result = ""
		self.separator = separator
		self.isFirst = True
		self.columnName = columnName
	def transform(self): 
		return getValue(self.columnName)
	def accumulate(self, val):
		if self.isFirst:
			self.result += val
			self.isFirst = False
		else:
			self.result += self.separator + val
	def getResult(self): 
		return self.result

class average:
	def __init__(self, columnName):
		self.result = ""
		self.columnName = columnName
		self.count = 0
		self.sum = 0
	def transform(self): 
		value = getValue(self.columnName)
		try:
			return int(value)
		except ValueError:
			try:
				return float(value) 
			except ValueError:
				return 0
	def accumulate(self, val):
		self.count += 1
		self.sum += val
	def getResult(self): 
		return self.sum / self.count

class min:
	def __init__(self, columnName):
		self.result = ""
		self.columnName = columnName
		self.min = 0
		self.unset = True
	def transform(self): 
		value = getValue(self.columnName)
		try:
			return int(value)
		except ValueError:
			try:
				return float(value) 
			except ValueError:
				return 0
	def accumulate(self, val):
		if self.unset: 
			self.unset = False
			self.min = val
		elif self.min > val:
			self.min = val
	def getResult(self): 
		return "NaN" if self.unset else self.min

class max:
	def __init__(self, columnName):
		self.result = ""
		self.columnName = columnName
		self.max = 0
		self.unset = True
	def transform(self): 
		value = getValue(self.columnName)
		try:
			return int(value)
		except ValueError:
			try:
				return float(value) 
			except ValueError:
				return 0
	def accumulate(self, val):
		if self.unset: 
			self.unset = False
			self.max = val
		elif self.max < val:
			self.max = val
	def getResult(self): 
		return "NaN" if self.unset else self.max