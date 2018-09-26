import re

pattern = r"abcdef"
s = "abcdefghijklmn"

# re模块直接调用
l = re.findall(pattern, s)
print(l)

# compile对象调用
regex = re.compile(pattern)
l1 = regex.findall(s)
print(l1)


l = re.split(r"\s+", "Hello World nihao China")
print("split():", l)

s = re.sub(r"\s+", "#", "Hello World nihao China", 2)
print("sub():", s)

s = re.subn(r"\s+", "#", "Hello World nihao China")
print("sub():", s)
