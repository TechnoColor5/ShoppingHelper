import item

class shopping_list:
	item_list = []
	max_total = 0
	min_total = 0
	avg_total = 0

	def add_item(input_item):
		item_list.append(input_item)
		max_total += input_item.max_price
		min_total += input_item.min_price
		avg_total += input_item.get_average()

	def remove_item(input_item):
		try:
			item_list.remove(input_item)
		except:
			print("Item is not in list")

	# Outputs the shopping list and displays total
	# mode = 0, gets maximum prices
	# mode = 1, gets minimum prices
	def output(mode): # 0 = max, 1 = min
		if mode == 0:
			print("Maximum shopping list:")
		elif mode == 1:
			print("Minimum shopping list:")
		else:
			print("mode " + strt(mode) + " is not a correct mode. Use 0 for max, 1 for min, or use output() for average")
		for i in item_list:
			price = 0
			total = 0
			if mode == 0:
				price = i.max_price
				total = max_total
			elif mode == 1:
				price = i.min_price
				total = min_total

			print(i.name + str(price))
		print("Total: " + total)

	# If no argument is passed, gets the average prices
	def output():
		print("Average shopping list:")
		for i in item_list:
			print(i.name + i.get_average)
		print("Total: " + avg_total)