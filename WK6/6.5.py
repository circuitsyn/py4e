#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
 
#Starter Code
text = "X-DSPAM-Confidence: 0.8475"

#find position of space
pos = text.find(" ")

#splice value after found position, convert to float and store value of splices number
result = float(text[pos:])

#print result
print(result)

