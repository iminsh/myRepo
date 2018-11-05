#! python3

import re

lengthReg = re.compile(r'[a-zA-Z0-9]{8,}')  # >= 8 letter or digit
digitReg = re.compile(r'\w*\d\w*')        # at least 1 digit
capitalReg = re.compile(r'\w*[A-Z]\w*')     # at least one capital letter
lowReg = re.compile(r'\w*[a-z]\w*')         # at least one low letter

while True:
    password = input('Please input passwrod: ')
    if password == 'exit':
        break

    if None == lengthReg.search(password):
        print('warning: at least 8 characters or digits')
        continue
    
    if None == digitReg.search(password):
        print('warning: at least 1 digit')
        continue

    if None == capitalReg.search(password):
        print('warning: at least 1 capital letter')
        continue
    
    if None == lowReg.search(password):
        print('warning: at least 1 low letter')
        continue

    print('Great. A strong password.')
    
