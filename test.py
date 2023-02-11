import re


items = re.findall(r'<(.*?)>', "./read <file_name> <var>")
print(items)
