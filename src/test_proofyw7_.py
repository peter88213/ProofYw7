"""Regression test for the proofyw7 script.

Test the conversion of the proofread-manuscript.

For further information see https://github.com/peter88213/PyWriter
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import unittest
import zipfile
from shutil import copyfile
from test_helper import TestBaseClass
from test_helper import read_file
import proofyw7_

UPDATE = False


class NrmOpr(TestBaseClass, unittest.TestCase):

    # The test methods must be defined here to identify the source of failure.

    def test_yw7_to_exp(self):
        """Test ODF export from yWriter. 
        
        Compare the generated content XML file with the reference file.
        """
        proofyw7_.main(self._testYwFile)
        with zipfile.ZipFile(self._testExpFile, 'r') as myzip:
            myzip.extract(self._odfCntntFile, self._execPath)
        if UPDATE:
            copyfile(f'{self._execPath}{self._odfCntntFile}', f'{self._dataPath}{self._odfCntntFile}')
        self.assertEqual(read_file(f'{self._execPath}{self._odfCntntFile}'),
                         read_file(f'{self._dataPath}{self._odfCntntFile}'))

    def test_imp_to_yw7(self):
        """Test ODF import to yWriter. 
        
        - Overwrite the initial yWriter project file.
        - Compare the generated yWriter project file with the reference file.
        - Compare the yWriter backup with the initial project file.
        """
        copyfile(self._prfImpFile, self._testImpFile)
        proofyw7_.main(self._testImpFile)
        if UPDATE:
            copyfile(self._testYwFile, self._prfYwFile)
        self.assertEqual(read_file(self._testYwFile), read_file(self._prfYwFile))
        self.assertEqual(read_file(self._ywBakFile), read_file(self._refYwFile))

    def test_data(self):
        super().test_data()


class ImportFromWord(TestBaseClass, unittest.TestCase):
    """Convert an ODT proofread document saved by MS Word."""

    def _init_paths(self):
        """Initialize the test data and execution paths."""
        super()._init_paths()
        self._prfImpFile = f'{self._dataPath}word.odt'
        self._prfYwFile = f'{self._dataPath}word.yw7'

    # The test methods must be defined here to identify the source of failure.

    def test_imp_to_yw7(self):
        """Test ODF import to yWriter. 
        
        - Overwrite the initial yWriter project file.
        - Compare the generated yWriter project file with the reference file.
        - Compare the yWriter backup with the initial project file.
        """
        copyfile(self._prfImpFile, self._testImpFile)
        proofyw7_.main(self._testImpFile)
        if UPDATE:
            copyfile(self._testYwFile, self._prfYwFile)
        self.assertEqual(read_file(self._testYwFile), read_file(self._prfYwFile))
        self.assertEqual(read_file(self._ywBakFile), read_file(self._refYwFile))

    def _remove_all_tempfiles(self):
        super()._remove_all_tempfiles()

    def test_data(self):
        pass


class ImportFromGoogledocs(TestBaseClass, unittest.TestCase):
    """Convert an ODT proofread document saved by MS Word."""

    def _init_paths(self):
        """Initialize the test data and execution paths."""
        super()._init_paths()
        self._prfImpFile = f'{self._dataPath}googledocs.odt'
        self._prfYwFile = f'{self._dataPath}googledocs.yw7'

    # The test methods must be defined here to identify the source of failure.

    def test_imp_to_yw7(self):
        """Test ODF import to yWriter. 
        
        - Overwrite the initial yWriter project file.
        - Compare the generated yWriter project file with the reference file.
        - Compare the yWriter backup with the initial project file.
        """
        copyfile(self._prfImpFile, self._testImpFile)
        proofyw7_.main(self._testImpFile)
        if UPDATE:
            copyfile(self._testYwFile, self._prfYwFile)
        self.assertEqual(read_file(self._testYwFile), read_file(self._prfYwFile))
        self.assertEqual(read_file(self._ywBakFile), read_file(self._refYwFile))

    def _remove_all_tempfiles(self):
        super()._remove_all_tempfiles()

    def test_data(self):
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
