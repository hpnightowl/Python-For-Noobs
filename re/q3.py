import re
line = "abbbs"
pattern = re.compile(r"ab+")
find = pattern.findall(line)
print(find)