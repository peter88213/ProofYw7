"""Build a Python script for the proofyw7 distribution.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the pywriter package.

The PyWriter project (see see https://github.com/peter88213/PyWriter)
must be located on the same directory level as the proofyw7 project. 

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/proofyw7
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../PyWriter/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}proofyw7_.py'
TARGET_FILE = f'{BUILD}proofyw7.py'


def main():
    # inliner.run(SOURCE_FILE, TARGET_FILE, 'proofyw7lib', '../src/', copyPyWriter=False)
    # inliner.run(TARGET_FILE, TARGET_FILE, 'pywriter', '../../PyWriter/src/', copyPyWriter=False)
    inliner.run(SOURCE_FILE, TARGET_FILE, 'proofyw7lib', '../src/')
    inliner.run(TARGET_FILE, TARGET_FILE, 'pywriter', '../src/')
    print('Done.')


if __name__ == '__main__':
    main()
