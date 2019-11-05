from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

tags = list()
# count = 0
# completed = 0
status = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def openUrl(url) :
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    global status
    # Retrieve all of the anchor tags
    tags = soup('a')
    print("count before", count)
    # print("status before", status)

    for tag in range(0, position):
        current = tags[tag]
        latestURL = current.get('href', None)
        print(current.get('href', None))
    status += + 1
    print("count", count)
    print("status", status)

    while(status < count) :
        openUrl(latestURL)
        print("count inside", count)
        print("status inside", status)
    return latestURL

# def scanData(tags) :
#     print("in scanndata")
#     print('TAGs:', tags)
    
#     for tag in tags:
#         count = count + 1
#         print("Count:", count)
#         if(count <= position) :
#             print("completed", completed)
#             while(completed < howMany) :
#                 print("completed", completed)
#                 completed = completed + 1
#                 # Look at the parts of a tag
#                 print('TAG:', tag)
#                 print('URL:', tag.get('href', None))
#                 print('Contents:', tag.contents[0])
#                 print('Attrs:', tag.attrs)
#         else :
#             quit()

# def printTag(tags) :
#     print("tags printed spec", tags)

url = input('Enter - ')
count = int(input('Count? '))
position = int(input('Position? '))

openUrl(url)

            
