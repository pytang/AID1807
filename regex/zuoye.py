import re

s = open('file.txt')

# pattern = r'[A-Z]\w*'
pattern = r'-?\d+\.?/?\d*%?'

l = []

for x in s:
    l += re.findall(pattern, x)
print(l)
