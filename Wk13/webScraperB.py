# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

tags = list()
count = 0
completed = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def openUrl(url) :
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    # print('TAGs first:', tags)

    for tag in range(0, position):
        print("Tag--: ", tags[tag])
        current = tags[tag]
        print(current.get('href', None))
        # print("Tag--: ", tag[tag].get('href', None))

    # scanData(tags)
    return tags

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
howMany = int(input('How many times? '))
position = int(input('Position? '))

openUrl(url)
# print("tags", tags)
# print('TAGs ouside:', tags)

            
