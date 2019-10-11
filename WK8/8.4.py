# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

#Desired output
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

#Starter code
fname = input("Enter file name: ")
fh = open(fname)
splitTxt = list()
finalLst = list()
#separate words and store in splitTxt
splitTxt = fh.read().split()
#print("splitTxt:", splitTxt)
#Sort text
sortedTxt = sorted(splitTxt)
#print("sortedTxt:", sortedTxt)
#for loop to create slimmer list of words
for word in sortedTxt:
    if word in finalLst : continue
    finalLst.append(word)

print(finalLst)
#print("sorted count:", len(sortedTxt))
#print("final count:", len(finalLst))

    