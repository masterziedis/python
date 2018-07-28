import re

url_regex = re.compile(
    r'(https?)://(www\.[A-za-z0-9-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search(
    "https://www.delfi.lt/veidai/zmones/prie-altoriaus-zenge-dainininkas-martynas-kavaliauskas-ir-jo-isrinktoji-rusne.d?id=78685633")
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
