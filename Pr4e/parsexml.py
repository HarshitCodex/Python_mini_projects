import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("enter url: ")
print('Retrieving', url)
raw = urllib.request.urlopen(url)
data=raw.read()
print('Retrieved',len(data),'characters')
print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print("Count: "+str(len(counts)))
sum = 0
for count in counts:
    sum+=int(count.text)
print("Sum:",sum)