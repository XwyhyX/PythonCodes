import os
def openTrans():
    #open file for appending
    with open('trans.log','a+') as f:
        nowBal = 0
        for line in f:
            parsed = line.split('$')
            nowBal = int(parsed[4])
    if nowBal is False:
        return 0
    else:
        return nowBal


def writeTrans(entryList,runningBal):
    translog = open('trans.log', 'a')
    translog.write(entryList[0] + '$' + entryList[1] + '$' + str(entryList[2]) + '$' + entryList[3] + '$' + str(runningBal))
    translog.write('\n')
    translog.close()
def check_if_empty(file):
    return os.stat(file).st_size == 0