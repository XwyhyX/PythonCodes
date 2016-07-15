#import average function
from statistics import mean as avg
#define dictionaries for login and grades
userdict = {'jrbenriquez':'password' , 'username':'password'}
studentdict = {"Aubrey":[98,89,78],"Carol":[78,81,88],"Vince":[87,79,92],"Michael":[96,92,98]}
#function for logging in
def logon():
    loginSuccess = 0
    while loginSuccess == 0:
        username = input('Enter Username: ')
        if username in userdict:
            passwordKey = userdict[username]
            password = input('Enter Password: ')
            if password == passwordKey:
                print('Login Successful')
                loginSuccess = 1
                print('\n---------------------\n')
            else:
                print('Password Incorrect')
        else:
            print('Username not found')
    exitgcentral = 0
    while exitgcentral == 0:
        x = gcentral()
        exitgcentral = x
#function for main program   
def gcentral():
    print('Welcome to Grade Central')
    print('\n')
    print('[1] Enter Grades')
    print('[2] Remove Student')
    print('[3] Student Average')
    print('[4] Exit')
    print('\n')
    taskNum = input('What do you want to do? ')
    
    if taskNum == '1':
        enterGrade()
        return 0
    elif taskNum == '2':
        removeStud()
        return 0
    elif taskNum == '3':
        studAvg()
        return 0
    elif taskNum == '4':
        exitgcentral = 1
        return exitgcentral
#function for entering grades 
def enterGrade():
    studentName = input('Student Name:')
    gradeInput = int(input('Grade:'))
    try:
        studentdict[studentName].append(gradeInput)
    except KeyError as keyErr:
        studentdict[studentName] = [gradeInput]
    print(studentdict)
#function for removing student
def removeStud():
    studentName = input('Student Name:')
    try:
        del studentdict[studentName]
    except KeyError as keyErr:
        print('Student',studentName,'not found')   
    print(studentdict)
    #function for getting average grade of student
def studAvg():
    studentName = input('Student Name:')
    try:
        average = avg(studentdict[studentName])
        print(studentName,'has an average grade of',average)
    except KeyError as keyErr:
        print('Student',studentName,'not found')   
    print(studentdict)
logon()
