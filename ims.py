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
time.sleep(1)
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

print "There are currently",len(set(numList)),"products in the inventory, and",len(numList),"entries in this database."
print
time.sleep(2)

# Ask user for their input
while True:
   command = raw_input("Would you like to [A]dd, [V]iew, [S]earch, e[X]port, or [E]xit? ")

# Multiple responses possible, allows for more flexibility
   responseList = ["A","a","Add","add","V","v","View","view","S","s","Search","search","X","x","Export","export","E","e","Exit","exit"]
   AresponseList = ["A","a","Add","add"]
   VresponseList = ["V","v","View","view"]
   SresponseList = ["S","s","Search","search"]
   XresponseList = ["X","x","Export","export"]
   EresponseList = ["E","e","Exit","exit"]

# If the user's response throws an error (and temporary command responses)
   if command not in responseList:
      print "Invalid response, please try again."
      print


   elif command in AresponseList:
      print "This function is still being developed."
      print


# View product list

#
# THIS CAN PROBABLY BE SHORTENED BY DEFINING A FUNCTION
#
   elif command in VresponseList:
      print "Available lists are"
      time.sleep(1.5)
      while True:
         command = raw_input("Which list would you like to view? ")   
         if command == "mfg":
            print mfgList
            time.sleep(1.5)
            print
            break
         elif command == "num":
            print numList
            time.sleep(1.5)
            print
            break
         elif command == "qty":
             print qtyList
             time.sleep(1.5)
             print
             break
         elif command == "cnd":
             print cndList
             time.sleep(1.5)
             print
             break
         elif command == "des":
             print desList
             time.sleep(1.5)
             print
             break
         elif command == "loc":
             print locList
             time.sleep(1.5)
             print
             break
         elif command == "lsl":
             print lslList
             time.sleep(1.5)
             print
             break
         elif command == "lcs":
             print lcsList
             time.sleep(1.5)
             print
             break
         elif command == "lpr":
             print lprList
             time.sleep(1.5)
             print
             break
         elif command == "nts":
             print ntsList
             time.sleep(1.5)
             print
             break
         elif command == "exit":
             print "Returning to main menu."
             time.sleep(1.5)
             clear()
             break
         else:
            print "List does not exist, please try again."
            print


   elif command in SresponseList:
      print "This function is still being developed."
      print
   elif command in XresponseList:
      print "This function is still being developed."
      print
   elif command in EresponseList:
      print "Exiting program."
      clear()
      break