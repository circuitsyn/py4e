# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

usrGrp = dict()

#function to process line
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
    if not line.startswith("From ") : continue
    #call function to process text data
    processor(line)

#Sorts tuple data and stores it in sortedData
sortedData = ( sorted( [ (x,y) for x,y in usrGrp.items() ] ) )

#runs a loop to print sorted final data
for x,y in sortedData :
    print(x,y)