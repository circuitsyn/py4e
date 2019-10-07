# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

#Desired output: Average spam confidence: 0.750718518519

#initialize starter variables
count = 0
confTotal = 0
currConf = 0

#initialize file handler to fname
fname = input("Enter file name: ")

#initialize file handler to fname
fh = open(fname)

#loop to go through each line of text
for line in fh:
    
    #skip lines not starting with desired text
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue

    #track counter for avgerage calculation
    count = count + 1
    #find position of space
    pos = line.find(" ")

    #splice value after found position, convert to float and store value of splices number
    currConf = float(line[pos:])
    #update total for later average
    confTotal = confTotal + currConf 

#calulate and store confidence value
confFinal = confTotal/count
#publish result average
print("Average spam confidence:", confFinal)
