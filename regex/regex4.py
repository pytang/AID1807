import re

s = "hello world"

pattern = r'Hello'

regex = re.compile(pattern, flags=re.I)

s = regex.search(s).group()

print(s)