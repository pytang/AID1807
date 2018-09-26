import re

pattern = r"(?P<dog>ab)cd(?P<pig>ef)"
regex = re.compile(pattern)

# 获取match对象
match_obj = regex.search('abcdefghi', pos=0, endpos=7)

# 属性变量
print(match_obj.pos)      # 匹配目标字符串的开始位置
print(match_obj.endpos)   # 匹配目标字符串的结束位置
print(match_obj.re)       # 正则表达式
print(match_obj.string)   # 目标字符串
print(match_obj.lastgroup)# 最后一个子组组名
print(match_obj.lastindex)# 最后一组第几组
print("======================================")

# 属性方法
print(match_obj.start())  # 匹配内容的开始位置
print(match_obj.end())    # 匹配内容的结束位置
print(match_obj.span())   # 匹配内容的起止位置

print(match_obj.group(0)) # 返回整个match对象内容
print(match_obj.group(2)) # 获取第二个子组匹配内容
print(match_obj.group('dog'))# 获取dog子组匹配内容

print(match_obj.groupdict)# 获取捕获组字典
print(match_obj.groups)   # 获取每个子组匹配内容
