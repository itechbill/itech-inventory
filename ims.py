# Application:		iTECH Trade Inventory Management System
# 				   	inventory.py
#				   	Manage warehouse inventory including stock
#				   	quantity, location, sales info etc.
# Author:			Bill O'Dwyer
# email:			   bill@itechtrade.co.uk
# Version:			0.1
# Date:				09/01/2015

import time,os,csv,string,itertools		      # For sleep, clear, list, separation, list handling

#Function to clear the screen
def clear():
	os.system('clear')

#Greet and load stock file
clear()
print "Welcome to the iTECH Trade Inventory Management System."
time.sleep(1.5)
print "Version 0.1			  bill@itechtrade.co.uk"
time.sleep(3)
clear()

#Open stock database
while True:
   try:
      database = csv.DictReader(open("stock.csv", "rb"), delimiter=",", quotechar='"')
      break
   except:
      print "Please ensure that a stock inventory file is located in this directory with the name stock.csv"

# Create empty lists for
mfgList = []				# Manufacturer
numList = []				# Product Number
qtyList = []				# Quantity
cndList = []				# Condition
desList = []            # Description
locList = []				# Location
lslList = []				# Last sale
lcsList = []				# Last customer
lprList = []				# Last price
ntsList = []				# Notes

# Scan file and put each field into a list
for row in database:
   mfgList.append(row.get("Manufacturer"))
   numList.append(row.get("Product Number"))
   qtyList.append(row.get("Quantity"))
   cndList.append(row.get("Condition"))
   desList.append(row.get("Description"))
   locList.append(row.get("Location"))
   lslList.append(row.get("Last Sale"))
   lcsList.append(row.get("Last Customer"))
   lprList.append(row.get("Last Price"))
   ntsList.append(row.get("Notes"))
   
#Ask user for their input
while True:
   command = raw_input("Would you like to [A]dd, [S]earch, e[X]port, or [E]xit? ")

# Multiple responses possible, allows for more flexibility
   responseList = ["A","a","Add","add","S","s","Search","search","X","x","Export","export","E","e","Exit","exit"]
   AresponseList = ["A","a","Add","add"]
   SresponseList = ["S","s","Search","search"]
   XresponseList = ["X","x","Export","export"]
   EresponseList = ["E","e","Exit","exit"]

# If the user's response throws an error (and temporary command responses)
   if command not in responseList:
      print "Invalid response, please try again."
      print
   elif command in AresponseList:
      print "Add."
      print "Thank you."
      break
   elif command in SresponseList:
      print "Add."
      print "Thank you."
      break
   elif command in XresponseList:
      print "Add."
      print "Thank you."
      break
   elif command in EresponseList:
      print "Add."
      print "Thank you."
      break

# if command == A
# bring up blank product card with cursor at first field
# ask to save changes when complete

# if command == S
# bring up search card and select field
# search results return quickly

# if command == X
# choose file format
# choose save location

# if command == E
# save the stock file
# close the stock file
# close the program