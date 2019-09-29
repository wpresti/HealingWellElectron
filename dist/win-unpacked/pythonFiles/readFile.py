import sys
import csv
import collections
from collections import Counter

def return_more_than_N(myList,N): #list,number N for count <=N
    counts = Counter(myList)
    out_list = [i for i in counts if counts[i]<=N]
    return out_list

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
        head = (next(readCSV))
        
        studentIndex = head.index("Present Students")
        print("student index", studentIndex)
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

        #print("\n------")
        #print(finalString)
        L = finalString.split(",")
        #print("\n----")
       # print("L is \n")
       # print(L)

        #print("\n----\n----")

    

        NOrLessList = return_more_than_N(L,N)
        # d = {}
        # d = collections.defaultdict(int)
        # for x in L: d[x] += 1
        # L[:] = [x for x in L if d[x] <= N]
        #print("list of ppl who show once", L)
        #print(type(L))
        print(N)
        print("\n")
        sortedL = sorted(NOrLessList)
        print(*sortedL,sep=', ',flush=True)
       
        #print(*sortedL, sep=', ',flush=True)
        #/Users/Will/Desktop/ViewList.csv

    #end if
else:
    print("no input file")