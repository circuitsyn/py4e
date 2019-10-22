import re

def processor(line) :
    collection = line.split()
    starterTime = collection[5]
    #print("starter time:",starterTime)
    hrCap = starterTime.split(":")
    #print("hr cap time:",hrCap)
    finishedData = hrCap[0]
    #code line that creates key and values for our dictionary
    usrGrp[finishedData] = usrGrp.get(finishedData,0) + 1
    return finishedData

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

#loop to go through each line of text
for line in fh:
    #skip lines not starting with desired text
    #if not line.startswith("From ") : continue
    #call function to process text data
    line = line.rstrip()
    processor(line)