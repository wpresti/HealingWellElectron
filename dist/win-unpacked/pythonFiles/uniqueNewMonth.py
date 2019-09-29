import sys
import csv
from datetime import datetime

total = 0
stopAtDate = False

if(len(sys.argv) > 1):
    dateCompareLow = None
    dateCompareHigh = None
    arg1 = sys.argv[1]
    print(arg1)
    if(len(sys.argv) == 4):
        startDate = sys.argv[2]
        endDate = sys.argv[3]
        stopAtDate = True
        print(startDate,endDate)
        if(len(startDate) != 0 and len(endDate) != 0):
            print("got here",startDate,endDate)
            dateCompareLow = datetime.strptime(startDate, '%Y-%m-%d').date()
            dateCompareHigh = datetime.strptime(endDate, '%Y-%m-%d').date()
    if(stopAtDate is False):
        print("Dates not entered")
        sys.exit()
    #oldMonthsSet = {}
    #newMonthSet = {}
    oldMonthsList = []
    newMonthList = []
    with open(arg1,'r') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        head = (next(readCSV))
        dateIndex = head.index("Attendance Date")
        studentIndex = head.index("Present Students")
        for row in readCSV:
            currDate = datetime.strptime(row[dateIndex],'%m-%d-%y').date()
            studentsString = row[studentIndex]
            #print("string!!",studentsString)
            studentsList = studentsString.split(',')
            print("array",studentsList)

            if(currDate < dateCompareLow): #dateCompareLow is not None and dateCompareHigh is not None and
                print(currDate,"is LOW of range")
                oldMonthsList.append(studentsList)
                #oldMonthsSet.update(studentsList) # list
                # add to set oldMonths
            if(currDate <= dateCompareHigh and currDate >= dateCompareLow):
                print(currDate,"is IN range")
                newMonthList.append(studentsList)
                #add to new set
            if(currDate > dateCompareHigh):
                print(currDate,"is PAST range")
                #do nothing for this row
                continue

            print(currDate,row[studentIndex])

    flattened_oldMonthsList = [y for x in oldMonthsList for y in x]
    flattened_newMonthList = [y for x in newMonthList for y in x]


    oldMonthsSet = set(flattened_oldMonthsList)
    newMonthSet = set(flattened_newMonthList)
    newPPlSet = newMonthSet - oldMonthsSet
    print(len(newPPlSet))

else:
    print("no input file")