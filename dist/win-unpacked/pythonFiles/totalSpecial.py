import sys
import csv
if(len(sys.argv) > 1):
    arg1 = sys.argv[1]
    with open(arg1,'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        head = (next(readCSV))
        numPresIndex = head.index("Number Of Present Students")
        classIndex = head.index("Class")
        #print(numPresIndex,classIndex)
        for row in readCSV:
            className = row[classIndex]
            classNumStud = row[numPresIndex]
            if className == 
            print(className,classNumStud)


else:
    print("no input file")