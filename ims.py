# Think Bakery.dos
# Open inventory file read/write
# Can add/remove stock/quantity
# Can search for stock
# Price data on as much as possible (last sale date/price/customer)
# Extra notes (inquiries, blocks on other orders, etc)

# Application:		iTECH Trade Inventory Management System
# 					inventory.py
#					Manage warehouse inventory including stock
#					quantity, location, sales info etc.
# Author:			Bill O'Dwyer
# email:			bill@itechtrade.co.uk
# Version:			0.1
# Date:				09/01/2015

import time,os

#Function to clear the screen
def clear():
	os.system('clear')

#Greeting
print "Welcome to the iTECH Trade Inventory Management System."
time.sleep(1.5)
print "Version 0.1			  bill@itechtrade.co.uk"
time.sleep(3)

clear()
print "Would you like to [A]dd, [S]earch, e[X]port, or [E]xit?"
