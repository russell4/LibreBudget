#!/usr/bin/python3

# This program is licensed under GPLv3+
# Author: Russell Brinson
# The idea for this type of progam came from the privacy focused matrix group. The idea centers around keeping data, processing, and formatting/presentation seperate. Normally a budget would be kept in a spreadsheet format where each of the above objects are together and end up conflicting with each other. Another benefit of seperating these objects is that each can be version controlled. The transaction and budget data can be traced back for analysis on errors or insight, the processing program can be edited to allow new functions and be rolled back if needed, and the formatting can be keep up to date without breaking other functions. 
# Input Files Needed: 
# 		- Budget in csv (comma delimited) This format should be the following
#			- Parent Category, Child Category, Budget Amount, Envelope
#			- String, String, Float, Yes/No
#		- Transaction in csv (comma delimited) This format should be the following 
#			- "TransactionID, Parent Category, Child Category, Payor/Payee, Transaction Amount, Date" <- should be top line without quotes
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

import csv

# Running this function will take the transaction file and total all transactions based on category in a Parent Category, Child Category, Actual Amount csv output
# Need to add - customer csv files names for inputs (based on args passed)
# https://stackoverflow.com/questions/25485681/creating-a-nested-dictionary-from-a-csv-file-with-python
def totalCategoryActualTransactionCSV():
	with open('fauxTransactions.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',') #possible ability to change delimiter
		line_count = 0
		
		childCatTotalDict = {} # dictionary of totals
		parentCatArray = () # array of dictionary
		
		for row in csv_reader:
			print(row)
			print(line_count)

			if line_count == 0:
				line_count += 1
			
			else:
				parentCat = row['Parent Category']
				childCat = row['Child Category']
				transAmount = row['Transaction Amount']
				
				# Check if parentCat does not exist in list already then create it
				if parentCat not in parentCatArray:
					parentCatArray.append(parentCat)
				'''
				# Does the child category exist in the parent?
				if childCat in parentCatArray[parentCat]:
					parentCatArray[i]{childCat}['Total Actual'] += transAmount
				else:
					parentCatArray[i]{}.update(['Child Category']:childCat, ['Total Actual']:transAmount)
				
				# lets me make sure to skip over the title line and how many lines processed
				line_count += 1
	
	# Printing to stdout for now for testing then will print to csv 
	for i in parentCatArray:
		for j in i:
			print(f'{Parent Category}, {Child Category}, {Total Actual}')
	'''
	#output_file = open('fauxTotalCategoryActual.csv', mode='w')
	#output_writer = csv.DictWriter(output_file) #"Parent Category, Child Category, Total Actual




	
def main():
	totalCategoryActualTransactionCSV()
	return 1
	
if __name__ == "__main__":
	main()
# Note: Yes/No should also accept YES, NO, yes, no with any captialization arraignment

