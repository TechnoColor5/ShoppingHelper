class item:
	def __init__(self, name, price) :
		self.name = name
		self.min_price = price
		self.max_price = price
		self.total = price
		self.num = 1

	def get_average(self):
		return round(self.total / self.num, 2)

	def add_price(self, input_price):
		self.total += input_price
		self.num += 1
		if input_price > self.max_price:
			self.max_price = input_price
		if input_price < self.min_price:
			self.min_price = input_price
