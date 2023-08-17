"""ProofYw7 - Import and export yw7 scenes for proofing. 

Proof reading file format: ODT (OASIS Open Document format) 
with visible scene tags.

Version @release
Requires Python 3.6+

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/ProofYw7
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
SUFFIX = '_proof'

import sys
import argparse
from pywriter.ui.ui import Ui
from pywriter.ui.ui_tk import UiTk
from proofyw7lib.proofyw_converter import ProofYwConverter


def main(sourcePath, silentMode=True, suffix=''):
    if silentMode:
        ui = Ui('')
    else:
        ui = UiTk('Import and export yw7 scenes for proofing')
    converter = ProofYwConverter()
    converter.ui = ui
    kwargs = {'suffix': suffix}
    converter.run(sourcePath, **kwargs)
    ui.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Import and export yw7 scenes for proofing',
        epilog='')
    parser.add_argument('sourcePath', metavar='Sourcefile',
                        help='The path of the file to convert.')
    parser.add_argument('--silent',
                        action="store_true",
                        help='suppress error messages and the request to confirm the use of default values')
    args = parser.parse_args()
    main(args.sourcePath, args.silent, SUFFIX)
