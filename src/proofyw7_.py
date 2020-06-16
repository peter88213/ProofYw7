"""ProofYw7 - Import and export yWriter 6/7 scenes for proofing. 

Proof reading file format: ODT (OASIS Open Document format) 
with visible chapter and scene tags.
Proofed file format: HTML with visible chapter and scene tags.

Depends on the PyWriter library v1.6

Copyright (c) 2020 Peter Triesberger
For further information see https://github.com/peter88213/ProofYw7
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import os

from pywriter.globals import *
from pywriter.odt.odt_proof import OdtProof
from pywriter.html.html_proof import HtmlProof
from pywriter.yw.yw_file import YwFile
from pywriter.converter.yw_cnv import YwCnv


def delete_tempfile(filePath):
    if filePath.endswith('.html'):
        try:
            os.remove(filePath)
        except:
            pass


def run(sourcePath):
    sourcePath = sourcePath.replace('file:///', '').replace('%20', ' ')
    converter = YwCnv()

    # The conversion's direction depends on the sourcePath argument.

    fileName, FileExtension = os.path.splitext(sourcePath)

    if FileExtension in ['.yw6', '.yw7']:
        document = OdtProof(fileName + PROOF_SUFFIX + '.odt')
        ywFile = YwFile(sourcePath)
        message = converter.yw_to_document(ywFile, document)
        return message

    elif sourcePath.endswith(PROOF_SUFFIX + '.html'):
        document = HtmlProof(sourcePath)

        # Determine the project file path.

        ywPath = sourcePath.split(PROOF_SUFFIX + '.html')[0] + '.yw7'

        if not os.path.isfile(ywPath):
            ywPath = sourcePath.split(PROOF_SUFFIX + '.html')[0] + '.yw6'

            if not os.path.isfile(ywPath):
                ywPath = None
                message = 'ERROR: No yWriter project found.'

        if ywPath:
            ywFile = YwFile(ywPath)
            message = converter.document_to_yw(document, ywFile)

        delete_tempfile(sourcePath)
        return message

    else:
        delete_tempfile(sourcePath)
        return 'File must be .yw7, .yw6, or _proof.html type.'


if __name__ == '__main__':
    try:
        sourcePath = sys.argv[1]

    except:
        files = os.listdir('.')

        sourcePath = None

        for file in files:

            if '.yw7' in file:
                sourcePath = file
                break

            if '.yw6' in file:
                sourcePath = file
                break

        if not sourcePath:
            sys.exit('ERROR: No yWriter project found.')

    print(run(sourcePath))
