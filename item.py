class item:
	def __init(self, name, price) :
		self.name = name
		self.price = price
		self.min_price = price
		self.max_price = price
		self.total += price
		self.num += 1
		self.get_average()

	def get_average(self):
		self.avg = self.total / self.num
