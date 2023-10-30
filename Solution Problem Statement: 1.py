import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter url to parse :')
try:
    response = urllib.request.urlopen(address, context=ctx)
    data = response.read()
    print("Data retrieved successfully.")
except Exception as e:
    print("An error occurred while retrieving the data:", str(e))
    exit()
tree = ET.fromstring(data)
counts = tree.findall('.//count')  # This will find all <count> elements in the XML tree
sum = 0
for count in counts:
    sum += int(count.text)
print('Sum is : ', sum)
#List = tree.findall(comments/comment/name/count)
