class sqlConstructor():

	sql    = ""
	dbName = ""
	query  = ""

	# Peripheral
	field_select = ""

	def setDatabase(self, dbName):
		""" Set Database """
		self.dbName = dbName
		return self

	def setQuery(self, mode, peripheral=""):
		""" Set query mode """
		if self.dbName == "":
			raise Exception("ERROR! Database name not set, you can set database name by using setDatabase('dbName')")

		if mode == 'INSERT_SET':
			self.query = "INSERT INTO `{}` SET ".format(dbName)
		
		elif mode == 'SELECT_ALL'
			self.query = "SELECT * "
		
		elif mode == 'SELECT_FIELD'
			if self.field_select == "":
				raise Exception("ERROR! Selected Field not set, you need to set the selected field first")
			self.query = "SELECT {} ".format()

		return self

	def 