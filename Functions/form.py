class form():
	
	form_group = []
	
	def __init__(self, load_data=False):
		self.form_group = []
		if load_data:
			self.load(load_data)

	def set_primary_key(self, id):
		self.form_group.append({
			'value' : id,
			'type'  : 'id'
		})

	""" Internal form data management """
	def load(self, load_data):
		""" Loading data from existing mappy form format"""
		self.form_group = load_data
		return self

	# [V1 Soon Deprecated, use data() instead]
	def get(self):	
		return self.form_group
	#########################################

	def data(self):
		return self.form_group

	def unpack(self):
		pass

	""" Form Elements """
	def text(self, label, placeholder, value=""):
		self.form_group.append({
			'label'       : label,
			'type'        : 'text',
			'placeholder' : placeholder,
			'value'       : value,
			'required'    : True,
		})

	def select(self, label, placeholder, option, value=""):
		self.form_group.append({			
			'label'       : label,
			'type'        : 'select',
			'placeholder' : placeholder,
			'value'       : value,
			'option'      : option,
			'required'    : True
		})

	