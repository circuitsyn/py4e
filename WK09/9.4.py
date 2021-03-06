#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

count = 0
usrGrp = dict()
winnerCount = None
winnerEmail = None

#function to process line
def processor(line) :
    collection = line.split()
    finishedData = collection[1]
    #print(finishedData)
    #code line that creates key and values for our dictionary
    usrGrp[finishedData] = usrGrp.get(finishedData,0) + 1
    return finishedData

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

#loop to go through each line of text
for line in fh:
    #skip lines not starting with desired text
    if not line.startswith("From:") : continue
    #call function to process text data
    processor(line)
    for email,count in usrGrp.items():
        if winnerCount is None or count > winnerCount:
            winnerEmail = email
            winnerCount = count
#print(usrGrp)
print(winnerEmail,winnerCount)
#print("There were", count, "lines in the file with From as the first word")
