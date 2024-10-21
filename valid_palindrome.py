import re

string = input("enter string: ")
step1 = string.casefold()
result = re.sub(r'[^a-z0-9]', '', step1)
reversed_string = result[::-1]
if result == reversed_string:
    print('true')
else:
    print('false')
