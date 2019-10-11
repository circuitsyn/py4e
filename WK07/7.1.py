#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

#Sample Code
# Use words.txt as the file name
#prompt for file name
fname = input("Enter file name: ")

#create handle for access to file
fh = open(fname)

#store file text as string
string = fh.read()

#strip white space
string.rstrip()

#turn string data to uppercase
upperV = string.upper()

#print file text data result
print(upperV)
