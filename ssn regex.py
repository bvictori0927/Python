#importing the regex module 

import re

#text I will be searching
sample= "FK rCXlQFbzBi-ycD639 88 0024mSnqE rXNy-DT fCeuNiS396 57 3329TluZRkN-BQjiTsGsmjoDpHoMIwRKPpbfHJ882 61 9767cOFHfAXSR--nDTS-UwzEBxRsm652 95 6590NZ -lTzJRAnJaqouYDpsrW079 13 7369Q BOW-bCWS  rH-X VhlDYN -ZMJb817 72 5478uzWGfkGYMXIkVQeMsPApT001 26 9198sbAoL m dpqVCBIMd"

#searching 

expression = re.compile(r'(\d{3,9}\s(\d{2})\s(/d{4})')


matches = pattern.finditer(sample)

for match in matches:
	print(match)
