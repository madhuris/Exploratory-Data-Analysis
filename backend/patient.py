class Patient(object):
	def __init__(self, id, diseases = {}, medications = {}, symptoms = {}, first_name = '', last_name = '', date_of_birth = '', gender = '', place = ''):
		# TODO : This needs to be in some util and not at Patients class level
		self.id = id
		self.diseases = diseases
		self.medications = medications
		self.symptoms = symptoms
		self.first_name  = first_name
		self.last_name  = last_name
		self.date_of_birth  = date_of_birth
		self.gender  = gender # TODO : Should be enum
		self.place = place

