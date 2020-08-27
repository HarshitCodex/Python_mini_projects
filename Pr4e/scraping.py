import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url - ')
count = int(input("Enter Count: "))
position = int(input("Enter Position: "))

names = []

while count > 0:
    print("retr :{0}".format(url))
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup('a')
    name = anchors[position - 1].string
    names.append(name)
    url = anchors[position - 1]['href']
    count -= 1

print(names[-1])
