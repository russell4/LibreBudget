'''
#!/usr/bin/python3

# This program is licensed under GPLv3+
# Author: Russell Brinson
# The idea for this type of progam came from the privacy focused matrix group. The idea centers around keeping data, processing, and formatting/presentation seperate. Normally a budget would be kept in a spreadsheet format where each of the above objects are together and end up conflicting with each other. Another benefit of seperating these objects is that each can be version controlled. The transaction and budget data can be traced back for analysis on errors or insight, the processing program can be edited to allow new functions and be rolled back if needed, and the formatting can be keep up to date without breaking other functions. 
# Input Files Needed: 
# 		- Budget in csv (comma delimited) This format should be the following
#			- Parent Category, Child Category, Budget Amount, Envelope
#			- String, String, Float, Yes/No
#		- Transaction in csv (comma delimited) This format should be the following 
#			- "TransactionID, Parent Category, Child Category, Payor/Payee, Transaction Amount, Date" <- should be top row without quotes
#			- Int, String, String, String, Float, String
#		- Python Budgeting file
#			- Other functions added to the file (and if published shared under the license)
# 		- Python Formatting file
#			- Other formatting features added to the file as needed
#			- Haven't decided on default output leaning torward markdown or LaTeX
#
# First milestone of the project is to calculated actual cost - To do this we need to:
# 	- Read the transaction file in
# 	- Add up transactions of same categories
'''
import csv



def totalChildTransactions(csvfile_name):
	# Need to add - customer csv files names for inputs (based on args passed)
	with open(csvfile_name, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',') #possible ability to change delimiter
		
		parentCatArray = uniqueCats(csvfile_name, 1) # gathers all parent categories
		totalsDict = dict()
		
		for item in parentCatArray:
			parentCat = item
			
			childDict = createSubCatDict(parentCat, csvfile_name) #finds all child cat for a given parent
			parentDict = {parentCat: childDict} #assigns all child cat to a given parent
			totalsDict.update(parentDict) #adds parent into the totals dictionary
			
		return totalsDict

def uniqueCats(csvfile_name, col):
	# Return array with unique categories from transaction csv based on column sent
	# col 1 - Parent Categories
	# col 2 - Child Categories
	with open(csvfile_name, mode='r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',') #possible future ability to change delimiter as optional definition arg
		line_count = 0
		
		uniqueArray = list()
		
		for row in csv_reader:
			if line_count == 0 and row[0] == "TransactionID":
				#print(row[col])
				line_count += 1
			else:	
				uniqueArray.append(row[col])
				line_count += 1
				
	return uniqueArray

def createSubCatDict(parentCategory, csvfile_name):
	# Totals all child categories of a given parent category
	subCatTotalsDict = dict()
	
	with open(csvfile_name, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',') #possible ability to change delimiter
		
		for row in csv_reader:
			if row['Parent Category'] == parentCategory: # This allows the creation of the dictionary all subcategories of a parent category
				childCat = row['Child Category'] # assign the child category to a variable
				if row['Child Category'] not in subCatTotalsDict:
					dictCreator = {childCat:0} # create the log if it doesn't exist
					subCatTotalsDict.update(dictCreator) # error if the dictionary entry isn't formatted before trying to update	
				subtotal = subCatTotalsDict[childCat] + int(row['Transaction Amount'])
				newTotal = {childCat:subtotal}
				subCatTotalsDict.update(newTotal)

	return subCatTotalsDict

def compareBudgetToActual(budgetDict, actualDict):
	#Both should be in the format of 
	#{'Parent Category':{'Child 1':-54, 'Child 2':609}}
	compDict = dict()
	
	for key in budgetDict:
		parentKey = dict()
		if key in actualDict:
			print(key)
			for child in budgetDict[key]:
				if child in actualDict[key]:
					difBudgetActual = budgetDict[key][child] - actualDict[key][child]
					
					print("\t"+child+": "+str(difBudgetActual))
				else:
					# Zero transactions against a bugdet, show original budget amount
					print("\t"+child+": N/A")
		else:
			# Parent category not in transactions
			print(key)
			for child in budgetDict[key]:
				# each child is also not in transactions
				difBudgetActual = budgetDict[key][child]
				print("\t"+child+": "+str(difBudgetActual))
	for key2 in actualDict:
		# need to filter all transactions that do not have a budget category
		if key2 not in budgetDict:
			print(key2)
			for child2 in actualDict[key2]:
				print("\t"+child2+": "+str(actualDict[key2][child2]))
				
		else:
			# need to check if any childs in transaction exist that budget does not have
			for child2 in actualDict[key2]:
				if child2 not in budgetDict[key2]:
					print(key2)
					print("\t"+child2+": "+str(actualDict[key2][child2]))
					
	''' ^^^ All the data can be gathered above for combining into compDict ^^^ '''
					

def main():
	TA_file = 'fauxTransactions.csv' # need to get from command line args
	BU_file = 'fauxBudget.csv'
	budgetTotals = {'House':{'Mortgage':700}, 'Utilities':{'Electricity':200,'Water':50}, 'Food':{'Groceries':100}, 'Car':{'Fuel':25, 'Maint':88}}
	
	actualTotals = totalChildTransactions(TA_file)
	compareBudgetToActual(budgetTotals, actualTotals)
	
	return 1
	
if __name__ == "__main__":
	main()
# Note: Yes/No should also accept YES, NO, yes, no with any captialization arraignment
#output_file = open('fauxTotalCategoryActual.csv', mode='w')
#output_writer = csv.DictWriter(output_file) #"Parent Category, Child Category, Total Actual
