import re

phone_number = "01033334444"
pat = re.compile("\d(?=\d{4})")
print(pat.sub("*", phone_number, count=0))
