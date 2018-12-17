from classes.item import item
from classes.receipt import receipt
from classes.shopping_list import shopping_list
import datetime
import openpyxl
import os.path

def check_item(item_name, item_price):
	add = True
	for i in item_master:
		if i.name == item_name:
			i.add_price(item_price)
			return
	#if you got this far, item does not exist
	item_master.append(item(item_name,item_price))

def read_wb(sheet):
	end = 'B' + str(sheet.max_row)
	for row in sheet['A1': end]:
		name = row[0].value
		price = row[1].value
		check_item(name, price)

def output_items(item_list):
	for i in item_list:
		print("Name: " + i.name + " Avg: " + str(i.get_average()) + " Max: " + str(i.max_price)
				+ " Min: " + str(i.min_price))

def add_item_to_master():
	name = input("Please enter the name of the item you wish to add: ")
	price = eval(input("Please enter the price for " + name + ": "))
	check_item(name, price)

def add_to_shop_list(shop_list):
	name = input("Please enter the item name: ")
	for i in item_master:
		if i.name == name:
			shop_list.add_item(i)
			return
	print("Item not found")

def remove_from_shop_list(shop_list):
	name = input("Please enter the item name: ")
	shop_list.remove_item(i)

def save_shop_list(shop_list):
	sheet_name = "List" + str(len(wb.worksheets) + 1)
	sheet = wb.create_sheet(sheet_name)
	item_list = shop_list.item_list

	for i in range(1, len(item_list) + 1):
		sheet.cell(row=i, column=1, value=item_list[i - 1].name)

def load_shop_list():
	sheet_name = input("Please enter the name of the list: ")
	shop_list = shopping_list()
	try:
		sheet = wb[sheet_name];
	except:
		print("That list does not exist")
		return None
	end = 'B' + str(sheet.max_row)
	for row in sheet["A1":end]:
		item_name = row[0].value;
		for i in item_master:
			if i.name == item_name:
				shop_list.add_item(i)
				break

	return shop_list

def shopping_menu(shop_list):
	while True:
		print("Now editing shopping list:")
		print("\t1. Add item to list")
		print("\t2. Remove item from list")
		print("\t3. Save list")
		print("\t4. Output list")
		print("\t0. Go Back")

		try:
			choice = eval(input("Please enter your choice: "))
		except:
			print("That is not a correct choice")
			continue
		print("\n--------------------\n")
		if choice == 1:
			add_to_shop_list(shop_list)
		elif choice == 2:
			remove_from_shop_list(shop_list)
		elif choice == 3:
			save_shop_list(shop_list)
		elif choice == 4:
			print("Which do you want:")
			print("\t1. Average prices")
			print("\t2. Maximum prices")
			print("\t3. Minimum prices")
			try:
				output_choice = eval(input("Please enter your choice: "))
				print("\n--------------------\n")
			except:
				print("That is not a correct choice")
				continue

			if output_choice == 1:
				shop_list.output()
			elif output_choice == 2:
				shop_list.output_mode(0)
			elif output_choice == 3:
				shop_list.output_mode(1)
		elif choice == 0:
			return

item_master = []
save_file = False

file_name = input("Please enter data file name: ")
if os.path.isfile(file_name): #if file exists, open it, else create it
	wb = openpyxl.load_workbook(file_name)
else:
	wb = openpyxl.Workbook()
	file_name = "data.xlsx"
	wb.create_sheet(0, 'Data')

if save_file:
	wb.save(file_name)

sheet = wb['Data']
read_wb(sheet)
output_items(item_master)

loop = True
while loop:
	print("What would you like to do?")
	print("\t1. Add an item")
	print("\t2. Start a new shopping list")
	print("\t3. Load a shopping list")
	print("\t4. Output item list")
	print("\t0. Quit")
	#load a shopping list?
	try:
		choice = eval(input("Please enter your choice: "))
	except:
		print("That is not a correct choice")
		continue
	print("\n--------------------\n")
	if choice == 1:
		add_item_to_master()
	elif choice == 2:
		shop_list = shopping_list()
		shopping_menu(shop_list)
	elif choice == 3:
		shop_list = load_shop_list()
		if shop_list is None:
			continue
		shopping_menu(shop_list)
	elif choice == 4:
		output_items(item_master)
	elif choice == 0:
		wb.save(file_name)
		loop = False
	print("\n--------------------\n")