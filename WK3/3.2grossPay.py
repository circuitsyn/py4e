try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r = float(rate)
#exception capture if there is an error
except:
    print("Make sure you are entering a number that is positive and larger than 0")
    quit()
result = 0
base = 0
overHrs = 0
overage = 0


#Check to see if overtime needs to be calculated and then do so if needed
if h > 40 :
    base = 40 * r
    overHrs = h - 40
    overage = ( r * 1.5 ) * overHrs
    result = base + overage
#check if hrs are under overtime and calculate pay if so
elif h <= 40 :
    result = h * r
#fallback if erronious item is given
else :
    print("Please confirm your hrs are positive and a real number!")

print(result)
