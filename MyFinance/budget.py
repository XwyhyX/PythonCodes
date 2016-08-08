import os

def addExpense(startingBalance):
	print("=================================")
	print("    Enter Expense:   " + "BAL>> " + str(currentBalance)+ " " + currency)
	print("=================================")
	expAmt = int(input(">> "))
	clearScreen()
	return startingBalance - expAmt
def addIncome(startingBalance):
	print("    Enter Income:   " + "BAL>> " + str(currentBalance)+ " " + currency)
	expAmt = int(input(">> "))
	clearScreen()
	return startingBalance + expAmt

def printBalance(currentBalance):
	print(" ")
	print("=================================")
	print("    CURRENT BALANCE IS:")
	print("                 >>>>> " +str(currentBalance) +" "+ currency)
	print("    (B) to go back")
	print("    (Enter) Another Expense")
	print("=================================")
	print(" ")
	stop_var = input(">> ")
	clearScreen()
	if stop_var == "":
		stop_var = " "
	if stop_var in "Bb":
		return "1" 
	else:
		return " "

def clearScreen():
	os.system('cls')

currency = "php"
endProg = 0
stop_opt = " "
clearScreen()
print("=================================")
print("    Starting amount: ")
print("=================================")
currentBalance = int(input(">> "))
clearScreen()

while endProg == 0:
	print("=========================================")
	print("                MAIN MENU ")
	print("=========================================")
	print("    [1] EXPENSE")
	print("    [2] INCOME")
	print("    [3] Exit         " + "BAL>> " + str(currentBalance)+ " " + currency)
	print("=========================================")
	print(" ")
	menuChoice = str(input(">> "))
	clearScreen()
	if menuChoice in "123":
		if menuChoice == "1":
			while stop_opt != "1":
				currentBalance = addExpense(currentBalance)
				stop_opt = printBalance(currentBalance)
				clearScreen()
			stop_opt = " "
		elif menuChoice == "2":
			while stop_opt != "1":
				currentBalance = addIncome(currentBalance)
				stop_opt = printBalance(currentBalance)
			stop_opt = " "
		elif menuChoice == "3":
			endProg = 1
	else:
		print("!!!!!!!!!!!!! Not a valid option !!!!!!!!!!!!!!!!!")