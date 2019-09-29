import sys
import csv
from datetime import datetime

total = 0
stopAtDate = False

if(len(sys.argv) > 1):
    dateCompare = None
    arg1 = sys.argv[1]
    if(len(sys.argv) == 3):
        endDate = sys.argv[2]
        if(len(endDate) != 0):
            dateCompare = datetime.strptime(endDate, '%Y-%m-%d').date()
            stopAtDate = True
    with open(arg1,'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        head = (next(readCSV))
        presStudentsIndex = head.index("Number Of Present Students")
        dateIndex = head.index("Attendance Date")
        for row in readCSV:
            if(stopAtDate is True):
                currDate = datetime.strptime(row[dateIndex],'%m-%d-%y').date()
                if(dateCompare is not None and currDate > dateCompare):
                    continue 
            studentCount = row[presStudentsIndex]
            studentCount = int(studentCount)
            print(type(studentCount),",",studentCount)
            total += studentCount
        
    print(total,flush=True)

else:
    print("no input file")