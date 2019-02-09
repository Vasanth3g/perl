class Car(object):
	"""
		blueprint for car
	"""

	def __init__(self, model, color, company, speed_limit):
		self.color = color
		self.company = company
		self.speed_limit = speed_limit
		self.model = model

	def start(self):
		print("started")
		print("%s was started" % (self.company))

	def stop(self):
		print("stopped")
		print("%s was stopped" % (self.company))

	def accelarate(self):
		print("accelarating...")
		"accelarator functionality here"

	def change_gear(self, gear_type):
		print("gear changed")
		" gear related functionality here"

x = Car("Audi", "black", "Audi", 60)
x.start()
x.stop()
