import re

with open('info.txt' 'r') as data:
    contents = data.read()

IP_Address = r'\b\d{3}\.\d{2}\.\d{2}\.\d{3}\b'

result = re.search(IP_Address, contents)

print(result.group())