import re
found = list()
totalItems = list()

fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "regex_sum_42.txt"
if len(fname) == 1 : 
    fname = "regex_sum_277128.txt"
fh = open(fname)

#loop to go through each line of text
for line in fh:
    line = line.rstrip()
    found = (re.findall('[0-9]+', line))
    #print("found: ", found)
    if len(found) < 1 : 
        continue
    else :
        for item in found :
            totalItems.append(int(item))

summedData = sum(totalItems)
average = summedData / len(totalItems)
    

# print("total items: ", totalItems)
# print("--------------------------------------")
print(summedData)
# print("--------------------------------------")
# print("avg: ", average)