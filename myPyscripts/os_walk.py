import os

for folderName, subfolders, filenames in os.walk('d:\\Repo'):
    print('current folder: ' + folderName)

    for subfolder in subfolders:
        print('subfolders in ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('files in ' + folderName + ': ' + filename)

    print('')
    
