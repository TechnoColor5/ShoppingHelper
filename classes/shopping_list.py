from .item import item

class shopping_list:
	item_list = []
	max_total = 0
	min_total = 0
	avg_total = 0
	name = ""

	def add_item(self, input_item):
		self.item_list.append(input_item)
		self.max_total += input_item.max_price
		self.min_total += input_item.min_price
		self.avg_total += input_item.get_average()
		self.round_totals()

	def round_totals(self):
		self.max_total = round(self.max_total, 2)
		self.min_total = round(self.min_total, 2)
		self.avg_total = round(self.avg_total, 2)

	def remove_item(self, input_item):
		try:
			self.item_list.remove(input_item)
		except:
			print("Item is not in list")

	# Outputs the shopping list and displays total
	# mode = 0, gets maximum prices
	# mode = 1, gets minimum prices
	def output_mode(self, mode): # 0 = max, 1 = min
		total = 0
		if mode == 0:
			print("\nMaximum shopping list:")
			total = self.max_total
		elif mode == 1:
			print("\nMinimum shopping list:")
			total = self.min_total
		else:
			print("mode " + strt(mode) + " is not a correct mode. Use 0 for max, 1 for min, or use output() for average")

		print("\tPrice\t" + "Item")
		for i in self.item_list:
			price = 0
			if mode == 0:
				price = i.max_price
			elif mode == 1:
				price = i.min_price

			print("\t" + str(price) + "\t" + i.name)
		print("Total: " + str(total) + "\n")

	# If no argument is passed, gets the average prices
	def output(self):
		print("\nAverage shopping list:")
		print("\tPrice\t" + "Item")
		for i in self.item_list:
			print("\t" + str(i.get_average()) + "\t" + i.name)
		print("Total: " + str(self.avg_total) + "\n")