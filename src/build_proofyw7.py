""" Build python scripts for the LibreOffice "proofread" script.
        
In order to distribute single scripts without dependencies, 
this script "inlines" all modules imported from the pywriter package.

The PyWriter project (see see https://github.com/peter88213/PyWriter)
must be located on the same directory level as the ProofYw7 project. 

For further information see https://github.com/peter88213/ProofYw7
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import inliner

SRC = '../src/'
BUILD = '../test/'


def main():
    os.chdir(SRC)
    inliner.run('proofyw7_.py', BUILD + 'proofyw7.py', 'pywriter')
    print('Done.')


if __name__ == '__main__':
    main()
