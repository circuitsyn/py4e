# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

#Starter Code
count = 0

#function to process line
def processor(line) :
    collection = line.split()
    finishedData = collection[1]
    print("email:", finishedData)
    return finishedData

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

#loop to go through each line of text
for line in fh:
    #skip lines not starting with desired text
    if not line.startswith("From:") : continue

    count = count + 1
    processor(line)
print("There were", count, "lines in the file with From as the first word")
