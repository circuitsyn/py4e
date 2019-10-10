# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#desired output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

#########################################################
count = 0
usrGrp = dict()
winnerCount = None
winnerEmail = None

#function to process line
def processor(line) :
    collection = line.split()
    starterTime = collection[5]
    #print("starter time:",starterTime)
    hrCap = starterTime.split(":")
    #print("hr cap time:",hrCap)
    finishedData = hrCap[0]
    #print("finished time:",finishedData)
    #code line that creates key and values for our dictionary
    usrGrp[finishedData] = usrGrp.get(finishedData,0) + 1
    return finishedData

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

#loop to go through each line of text
for line in fh:
    #skip lines not starting with desired text
    if not line.startswith("From ") : continue
    #call function to process text data
    processor(line)
    print("usr grp", usrGrp)
    # for email,count in usrGrp.items():
    #     if winnerCount is None or count > winnerCount:
    #         winnerEmail = email
    #         winnerCount = count
#print(usrGrp)
for (x,y) in usrGrp :
    print(x,y)
print(winnerEmail,winnerCount)
#print("There were", count, "lines in the file with From as the first word")