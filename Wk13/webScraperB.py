# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
complete = 0
url = input('Enter - ')
howMany = input('How many times?')
position = input('Position?')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    count = count + 1
    print("Count:", count)
    if(count == position) :
        print("completed", completed)
        while(completed < howMany) :
            completed = completed + 1
            # Look at the parts of a tag
            print('TAG:', tag)
            print('URL:', tag.get('href', None))
            print('Contents:', tag.contents[0])
            print('Attrs:', tag.attrs)
            
