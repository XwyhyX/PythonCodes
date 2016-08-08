import os

def addExpense(startingBalance,tranCount):
	print("=================================")
	print("    Enter Expense:   " + "BAL>> " + str(currentBalance)+ " " + currency)
	print("=================================")
	expAmt = int(input(">> "))
	print("=================================")
	amtDict[tranCount] = {expAmt:input("    Description: ")}
	expenseDict[tranCount] = amtDict[tranCount]
	print("=================================")
	clearScreen()
	return startingBalance - expAmt
def addIncome(startingBalance,tranCount):
	print("=================================")
	print("    Enter Income:   " + "BAL>> " + str(currentBalance)+ " " + currency)
	print("=================================")
	expAmt = int(input(">> "))
	print("=================================")
	amtDict[tranCount] = {expAmt:input("    Description: ")}
	incomeDict[tranCount] = amtDict[tranCount]
	print("=================================")
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
	
	
#===INDICATOR VARIABLES HERE ==========
tranCount = 0
currency = "php"
endProg = 0
stop_opt = " "
clearScreen()
#===Dictionary HERE  ==============
expenseDict = {}
incomeDict = {}
amtDict = {}
print("=================================")
print("    Starting amount: ")
print("=================================")
currentBalance = int(input(">> "))
clearScreen()

while endProg == 0:
	print("=========================================")
	print("                MAIN MENU ")
	print("=========================================")
	print( "  BAL>> " + str(currentBalance)+ " " + currency)
	print()
	print("    [1] EXPENSE         ")
	print("    [2] INCOME")
	print("    [3] EXIT")
	print("=========================================")
	print(" ")
	if len(amtDict) > 0 :
		print("=========================================")
		print("    TRANSACTIONS ")
		print("                  [S] to save transaction")
		print("=========================================")
		for i in range(0,len(amtDict)):
			if i in expenseDict.keys():
				tranInd = 'E'
			elif i in incomeDict.keys():
				tranInd = 'I'
			print("      " + str(amtDict[i]) + " - " + tranInd)
		
	menuChoice = str(input(">> "))
	clearScreen()
	if menuChoice in "123":
		if menuChoice == "1":
			while stop_opt != "1":
				currentBalance = addExpense(currentBalance,tranCount)
				tranCount = tranCount + 1
				stop_opt = printBalance(currentBalance)
				clearScreen()
			stop_opt = " "
		elif menuChoice == "2":
			while stop_opt != "1":
				currentBalance = addIncome(currentBalance, tranCount)
				tranCount = tranCount + 1
				stop_opt = printBalance(currentBalance)
			stop_opt = " "
		elif menuChoice == "3":
			endProg = 1
	if len(amtDict) > 0 :
		if menuChoice == "":
			pass
		elif menuChoice in "Ss":
			clearScreen()
			print("SAVING")
			input()
			clearScreen()
			print("SAVED!")
				