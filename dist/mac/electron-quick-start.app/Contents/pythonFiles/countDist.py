import sys
import csv
import collections
from collections import Counter


filePath = ""
people = []
total = 0

#script
if(len(sys.argv) > 1):
    arg1 = sys.argv[1]
    if(len(sys.argv) == 3):
        N = int(sys.argv[2])
    else:
        N = 1
    print("args",arg1,"\n")
    with open(arg1,'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        head = next(readCSV)
        studentIndex = head.index("Present Students")
        for row in readCSV:
            peopleComma = row[studentIndex]
            #print(peopleComma)
            peopleSplitArr = peopleComma.split(',')
            #print("peopleSPlitArr",(peopleSplitArr))
            pplStr = ", ".join(peopleSplitArr)
            #print("pplStr",pplStr)
            pplStr = pplStr.lower().title()
            #print("lowercase pplstr",pplStr)

            people.append(pplStr)

        #print("final list",people)
        finalString = ",".join(people)
        finalString = finalString.replace(", ",",")
        L = finalString.split(",")

        setNames = set(L)
        print(len(setNames))

       
        #/Users/Will/Desktop/ViewList.csv

    #end if
else:
    print("no input file")