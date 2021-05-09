class form():
	
	form_group = []
	
	def __init__(self, id):
		self.form_group = []
		self.form_group.append({
			'value' : id,
			'type'  : 'id'
		})

	def get(self):	
		return self.form_group

	def add_text(self, label, placeholder, value=""):
		self.form_group.append({
			'label'       : label,
			'type'        : 'text',
			'placeholder' : placeholder,
			'value'       : value,
			'required'    : True,
		})

	def add_select(self, label, placeholder, option, value=""):
		self.form_group.append({			
			'label'       : label,
			'type'        : 'select',
			'placeholder' : placeholder,
			'value'       : value,
			'option'      : option,
			'required'    : True
		})