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

# Test code output
# print("Data:", data.decode())

info = json.loads(data)
print('User Count:', len(info))

# store tree xml data in tree
# tree = ET.fromstring(data)
# pull count data from xml
# counts = tree.findall('.//count')

# for count in counts :
#     # print("count:", count)
#     total = total + int(count.text)
# print("total", total)