import re
text = "Last night geriau Mr. Alaus ir valgiau Ms. Pica"

pattern = re.compile(r'(Mr.|Mrs|Ms.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)
