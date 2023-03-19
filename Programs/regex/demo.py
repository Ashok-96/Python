import re
text=':)'
pattern=":\)"
result=re.finditer(pattern=pattern,string=text)
for i in result:
    print(i)