"""Find yWriter 7 project folders

Part of the yW2OO installation.
Create a batch file in order to copy "proof.bat" in each 
yWriter7 project folder.

This script is to be executed in the "setup" subfolder
of the yW2OO install folder. 

Copyright (c) 2020 Peter Triesberger.
For further information see https://github.com/peter88213/yW2OO
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os


documents = os.environ['USERPROFILE'] + '\\Documents'
pathList = []

for (path, dirs, files) in os.walk(documents):

    for fileName in files:

        if fileName.endswith('.yw7'):
            pathList.append(path)

cpy = ['echo Copy "proof.bat" in each yWriter7 project folder.\n']
rmv = ['echo Remove "proof.bat" from each yWriter7 project folder.\n']

for filePath in pathList:
    cpy.append('copy /y proof.bat "' + filePath + '"\n')
    rmv.append('del /q "' + filePath + '\\proof.bat"\n')

with open('copyproof.bat', 'w', encoding='utf-8') as f:
    f.writelines(cpy)

with open('removeproof.bat', 'w', encoding='utf-8') as f:
    f.writelines(rmv)
