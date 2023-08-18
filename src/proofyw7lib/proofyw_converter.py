"""Provide a converter class for yWriter 7 universal import and export.

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/PyWriter
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.converter.yw_cnv_ff import YwCnvFf
from pywriter.converter.new_project_factory import NewProjectFactory
from pywriter.yw.yw7_file import Yw7File
from pywriter.odt_w.odt_w_proof import OdtWProof
from pywriter.odt_r.odt_r_proof import OdtRProof


class ProofYwConverter(YwCnvFf):
    """A converter for universal import and export.

    Support yWriter 7 projects and most of the Novel subclasses 
    that can be read or written by OpenOffice/LibreOffice.

    Overrides the superclass constants EXPORT_SOURCE_CLASSES,
    EXPORT_TARGET_CLASSES, IMPORT_SOURCE_CLASSES, IMPORT_TARGET_CLASSES.

    Class constants:
        CREATE_SOURCE_CLASSES -- list of classes that - additional to HtmlImport
                        and HtmlOutline - can be exported to a new yWriter project.
    """
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [OdtWProof                             ]
    IMPORT_SOURCE_CLASSES = [OdtRProof]
    IMPORT_TARGET_CLASSES = [Yw7File]
    CREATE_SOURCE_CLASSES = []

    def __init__(self):
        """Change the newProjectFactory strategy.
        
        Extends the superclass constructor.
        """
        super().__init__()
        self.newProjectFactory = NewProjectFactory(self.CREATE_SOURCE_CLASSES)
        self.newProjectFactory.DO_NOT_IMPORT.append('')
