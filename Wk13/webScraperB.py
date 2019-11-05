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
    tags = soup('a')

    for tag in range(0, position):
        current = tags[tag]
        latestURL = current.get('href', None)
        print(current.get('href', None))
    status += + 1

    while(status < count) :
        openUrl(latestURL)
    return latestURL

url = input('Enter - ')
count = int(input('Count? '))
position = int(input('Position? '))

openUrl(url)

            
