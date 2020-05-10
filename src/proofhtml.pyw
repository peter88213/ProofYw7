"""Import and export ywriter7 scenes for proofing. 

Proof reading file format = html with visible chapter and scene tags.

Copyright (c) 2020, peter88213
For further information see https://github.com/peter88213/ProofYw7
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""

import sys

from pywriter.model.htmlfile import HtmlFile
from pywriter.converter.cnv_runner import CnvRunner


def run(sourcePath: str, silentMode: bool = True) -> None:
    document = HtmlFile('')
    converter = CnvRunner(sourcePath, document, 'html', silentMode)


if __name__ == '__main__':
    try:
        sourcePath = sys.argv[1]
    except:
        sourcePath = ''
    run(sourcePath, False)