import random

def generate_id(appendix):
	return "{}{}".format(appendix, str(random.randint(100000,999999)))