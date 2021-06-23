# Import all microclass for constructing data
from Functions.form import form
from Functions.option import option
from Functions.Table import Table
import random

def generateId(appendix):
	return "{}{}".format(appendix, str(random.randint(100000,999999)))

class Form(form):
	""" Form class for constructing form """
	pass

class Table(Table):
	""" Table class for constructing table """
	pass

class Options(option):
	pass

