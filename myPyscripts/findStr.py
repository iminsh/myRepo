#! python3
# finds lines matching regEx, in all .txt files in specific folder

import os, sys, re

#path
strPath = 'C:\\Users\\wuh\\AppData\\Local\\Continuum\\anaconda3\\myscripts'
#strPath = 'D:\\Temp'

if not os.path.exists(strPath):
    print('path not exist!')
    sys.exit(0)


#regEx text
#regTxt = input('regulation expresion: ')
regTxt = r'\d+'

regEx = re.compile(regTxt)

for filename in os.listdir(strPath):
    #print(filename)
    if '.py' == filename[-3:]:
        print(filename)
        f = open(os.path.join(strPath, filename))
        lines = f.readlines()
        for line in lines:
            if None != regEx.search(line):
                print(line)
            
        f.close()
        
