from datetime import date
from datetime import time

class receipt:
	def __init__(self, input_date):
		self.date_purchased = input_date

	item_list = []
	def add_item(self, purchased_item):
		item_list.add(purchased_item)
