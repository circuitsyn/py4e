import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

url = input('Enter - ')
if (len(url) < 1) :
    print("Check your URL!") 
    quit()
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)

for item in info['comments'] :
    total = total + int(item['count'])
print("Total:", total)