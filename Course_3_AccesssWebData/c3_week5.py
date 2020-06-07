from urllib.request import urlopen
import xml.etree.ElementTree as ET


url = input("Enter Location:")
print("Retrieving",url)

data = urlopen(url).read()
print("Retrieved:",len(data),"characters")
tree = ET.fromstring(data)


counts = tree.findall('.//count')
print("Count:",len(counts))

sum = 0
for count in counts:
    sum += int(count.text)

print('total: ', sum)