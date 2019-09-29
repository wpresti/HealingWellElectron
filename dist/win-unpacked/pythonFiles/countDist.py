
# counts unique number of people in programs and connections... basically everything but the special event stops at end date if given
import sys
import csv
import collections
from collections import Counter
from datetime import datetime



filePath = ""
people = []
total = 0
endDate = ""
stopAtDate = False

#script
if(len(sys.argv) > 1):
    dateCompare = None;
    arg1 = sys.argv[1]
    if(len(sys.argv) == 3):
        endDate = sys.argv[2] # month day year   09-17-19
        if(len(endDate) != 0):
            dateCompare = datetime.strptime(endDate, '%Y-%m-%d').date()
            stopAtDate = True
        print(dateCompare)
        #stopAtDate = True
    print("args",arg1,"\n")
    print("endDate",endDate)
    with open(arg1,'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        head = next(readCSV)
        studentIndex = head.index("Present Students")
        dateIndex = head.index("Attendance Date")
        classIndex = head.index("Class")
        for row in readCSV:
            if(stopAtDate is True):
                currDate = datetime.strptime(row[dateIndex],'%m-%d-%y').date()
                if(dateCompare is not None and currDate > dateCompare):
                    continue 
            if(row[classIndex] == "Special Event"):
                print("Special Event!!!")
                continue;
            peopleComma = row[studentIndex]
     
            peopleSplitArr = peopleComma.split(',')
        
            pplStr = ", ".join(peopleSplitArr)
            pplStr = pplStr.lower().title()
            #print("lowercase pplstr",pplStr)

            people.append(pplStr)

        #print("final list",people)
        finalString = ",".join(people)
        finalString = finalString.replace(", ",",")
        L = finalString.split(",")
        print("L is:",L)
        setNames = set(L)
        print("set",setNames)
        print(len(setNames))

       
        #/Users/Will/Desktop/ViewList.csv

    #end if
else:
    print("no input file")