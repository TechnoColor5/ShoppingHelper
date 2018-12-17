from classes.item import item
from classes.receipt import receipt
from datetime import date
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

def add_item():
	name = input("Please enter the name of the item you wish to add: ")
	price = eval(input("Please enter the price for " + name + ": "))
	check_item(name, price)

item_master = []
save_file = False

file_name = input("Please enter data file name: ")
if os.path.isfile(file_name): #if file exists, open it, else create it
	wb = openpyxl.load_workbook(file_name)
else:
	wb = openpyxl.Workbook()
	save_file = True

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
	print("\t3. Output item list")
	print("\t0. Quit")
	#load a shopping list?
	choice = eval(input("Please enter your choice: "))
	print("\n--------------------\n")
	if choice == 1:
		add_item()
	elif choice == 2:
		start_list()
	elif choice == 3:
		output_items(item_master)
	elif choice == 0:
		loop = False