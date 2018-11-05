#! python3
# phoneAndemail.py
# finds phone numbers and email addresses
# on the clipboard, which is copy from
# page of https://nostarch.com/contactus.

import pyperclip, re

# phone number regex
phoneReg = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator
    (\d{3})                 # first 3 digits
    (\s|-|\.)?              # separator
    (\d{4})                 # last 4 digits
    )''', re.VERBOSE)

# TODO
# email address regex

# TODO
# retrieve text from clipboard.
text = str(pyperclip.paste())

# find matches in the clipboard text.
matches = []
for tuples in phoneReg.findall(text):
    print(tuples[0])
    phonenum = '-'.join([tuples[1], tuples[3], tuples[5]])
    matches.append(phonenum)

# TODO
# copy results to the clipboard.

    
