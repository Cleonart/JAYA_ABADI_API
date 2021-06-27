class form():
	
	form_group = []
	defined_key = None

	def __init__(self, load_data=False):
		self.form_group = []
		if load_data:
			self.load(load_data)

	def set_primary_key(self, id):
		defined_key = self.defined_key
		self.form_group.append({
			'key' : defined_key,
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
		form_unpacked = {}
		for input in self.form_group:
			form_unpacked[input['key']] = input['value']
		return form_unpacked

	def key(self, defined_key):
		self.defined_key = defined_key
		return self

	""" Form Elements """
	def text(self, label, placeholder, value=""):
		defined_key = self.defined_key
		self.form_group.append({
			'key' : defined_key,
			'label' : label,
			'type' : 'text',
			'placeholder' : placeholder,
			'value' : value,
			'required' : True,
		})

	def select(self, label, placeholder, option, value=""):
		defined_key = self.defined_key
		self.form_group.append({
			'key' : defined_key,		
			'label' : label,
			'type' : 'select',
			'placeholder' : placeholder,
			'value' : value,
			'option' : option,
			'required' : True
		})

	