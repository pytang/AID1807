import re









# fullmatch
try:
    obj = re.fullmatch(r"\w+", "abcdef123")
    print(obj.group())
except AttributeError as e:
    print(e)

# match
obj = re.match(r"foo","foo,food on the table")
print(obj.group())

# search
obj = re.search(r"foo","foo,food on the table")
print(obj.group())