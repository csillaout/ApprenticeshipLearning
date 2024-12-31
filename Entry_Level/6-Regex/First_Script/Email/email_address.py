import re

with open('info.txt', 'r') as data:
    contents = data.read()

email_pattern = r'\w+@\w+\.\w+'

result = re.search(email_pattern, contents)

print(result.group())