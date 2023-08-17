"""Test helper module.

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/PyWriter
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
from shutil import copyfile
from abc import ABC


def read_file(inputFile):
    """Read a utf-8 or ANSI encoded text file.
    
    Positional arguments:
        inputFile -- str: path of the file to read.
        
    Return a string.
    """
    try:
        with open(inputFile, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        # HTML files exported by a word processor may be ANSI encoded.
        with open(inputFile, 'r') as f:
            return f.read()


class TestBaseClass(ABC):
    """Test case: Import and export yWriter project.
    
    Public methods:
        test_data() -- verify test data integrity.
        test_imp_to_yw7() -- test HTML/CSV import to yWriter, using the YwCnv converter class.
        test_imp_to_yw7_ui() -- test HTML/CSV import to yWriter, using the YwCnvUi converter class.
    
    Subclasses must also inherit from unittest.TestCase
    """

    def setUp(self):
        """Set up the test environment.
        
        - Initialize the test data and execution paths.
        - Make sure the directory for text execution exists.
        - Remove files that may remain from previous tests.
        - Create a test yWriter project.
        """
        self._init_paths()
        os.makedirs(self._execPath, exist_ok=True)
        self._remove_all_tempfiles()
        copyfile(self._refYwFile, self._testYwFile)

    def tearDown(self):
        """Clean up the test execution directory.
        
        This method is called by the unit test framework.
        """
        self._remove_all_tempfiles()

    def _init_paths(self):
        """Initialize the test data and execution paths."""
        if not hasattr(self, '_dataPath'):
            self._dataPath = f'../test/data/_proof/'
        self._execPath = '../test/tmp/'
        self._testExpFile = f'{self._execPath}yw7 Sample Project_proof.odt'
        self._odfCntntFile = 'content.xml'
        self._testYwFile = f'{self._execPath}yw7 Sample Project.yw7'
        self._ywBakFile = f'{self._testYwFile}.bak'
        self._refYwFile = f'{self._dataPath}normal.yw7'
        self._prfYwFile = f'{self._dataPath}proofed.yw7'
        self._testImpFile = f'{self._execPath}yw7 Sample Project_proof.odt'
        self._refImpFile = f'{self._dataPath}normal.odt'
        self._prfImpFile = f'{self._dataPath}proofed.odt'

    def test_data(self):
        """Verify test data integrity. 

        Initial test data must differ from the "proofed" test data.
        """
        self.assertNotEqual(read_file(self._refYwFile), read_file(self._prfYwFile))

    def _remove_all_tempfiles(self):
        """Clean up the test execution directory."""
        try:
            os.remove(self._testExpFile)
        except:
            pass
        try:
            os.remove(self._testYwFile)
        except:
            pass
        try:
            os.remove(self._ywBakFile)
        except:
            pass
        try:
            os.remove(f'{self._execPath}{self._odfCntntFile}')
        except:
            pass
        try:
            os.remove(self._testImpFile)
        except:
            pass

