import os
import datetime
from defs import *

now = datetime.datetime.now()
runningBal = 0

runningBal = openTrans()

print "Current Balance is %d" %(runningBal)

#GET DATE TRANSACTION
date=raw_input('Date (mm/dd/yyyy] [default:today]: ')
if date == '':
    date= str(now.month)+ "/" + str(now.day)+ "/" + str(now.year)
#GET TYPE OF TRANSACTION
transType=raw_input("[I]ncome or [E]xpense? [default:Income]: ")
choice_add = 'Ii '
choice_subtract = 'Ee'

#GET AMOUNT FOR TRANSACTION
amount = input('Amount: ')

#GET DESCRIPTION OF TRANSACTION
transDesc = raw_input('Describe Transaction: ')

entryList = [
    date,
    transType,
    amount,
    transDesc
]

if transType in choice_add:
    runningBal = runningBal + amount
elif transType in choice_subtract:
    runningBal = runningBal - amount
print "Current Balance After entry is %d" %(runningBal)
writeTrans(entryList,runningBal)
