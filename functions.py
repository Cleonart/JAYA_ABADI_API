# Import all microclass for constructing data
from Functions.form import form
from Functions.option import option
from Functions.table import table
import random

def generateId(appendix):
	return "{}{}".format(appendix, str(random.randint(100000,999999)))

class Form(form):
	""" Form class for constructing form """
	pass

class Table(table):
	""" Table class for constructing table """
	pass

class Options(option):
	pass

