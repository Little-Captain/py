import re

regex = '\s[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s]'
text = """This is some text with x@y.z embedded e-mails
that we'll use as@example.com
some lines have no email addresses
others@have.two valid email@address.com
The re module is awonderful@thing."""
print('** Search text ***\n'+text)
print('** Regex ***\n' + regex + '\n***')

utext = text.upper()

s = re.search(regex, utext)
if s:
    print('*** At least one email found "' + s.group() + '"')

m = re.findall(regex, utext)
if m:
    for match in m:
        print('Match found', match.strip())