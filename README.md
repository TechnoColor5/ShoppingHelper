# ShoppingHelper
ShoppingHelper is a tool that helps you estimate how much you will spend when you go shopping. I originally came up with this idea as a poor college student trying to figure out what I can afford to buy on a specific week for groceries. ShoppingHelper does this by having you input items and how much you paid for them. Each item holds an average, minimum and maximum price. When you add items to a shopping you list, it will tally up the total price for all of the items and ask you if you want to see what the list would cost going by the items' average, maximum, or minimum prices.

## How to use
1. Run program as `python3 shopping_helper.py`
2. Enter the name of the data file you wish to use
	1. If you type in a file that does not exist, one will be created
3. The program will load in all of the data from the file

## Data Input
ShoppingHelper collects its data from the user inputting the name of a .xlsx file that has a sheet named 'Data'. The file should be set up so that the name of the item is in column A and the price is in columb B. For example:

![example image](/images/img1.png)

If the file you enter 

## Saving/Loading Shopping Lists
Shopping lists are saved/loaded from the same data file as used in the beginning of running ShoppingHelper. When saved, the list will be added as another sheet with the name "List#" (# being a number). When loading a shopping list, the program will just ask for the *exact* name of the sheet that the list is housed under.

### Creating your own list
In case you want to create your own list and port it into ShoppingHelper that way, you can simply list the names of all of the items in column A of a sheet. **Make sure you name the items exactly like they are named in the 'Data' sheet**. If you do not name it correctly, the item will not show up in the program as being part of the list. An example of a shopping list can be seen below:

![Shopping List example](/images/img2.png)
