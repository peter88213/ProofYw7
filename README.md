# ProofYw7 - Proofread yWriter 7 scenes with LibreOffice

Export an yWriter 7 project to an OpenDocument file with chapter and scene markers. 
Write back the proofread scenes to the yWriter 7 project file.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot1.png)

For more information see [Wiki (english)](https://github.com/peter88213/ProofYw7/wiki)

## Requirements

* Windows.

* yWriter 7.

* A LibreOffice 5 or 6 standard installation (not a "portable" version).

## Download

The ProofYw7 Software comes as a zipfile `ProofYw7_<version number>.zip`. 

[Download page](https://github.com/peter88213/ProofYw7/releases)



## How to install

1. If you have already installed a version of ProofYw7, please run the uninstaller for it. 

2. Unzip `ProofYw7_<version number>.zip` within your user profile.

3. Move into the `ProofYw7_<version number>` folder and run `Install.bat` (double click).
   This will copy all needed files to the right places, install a LibreOffice extension.
   You may be asked for approval to modify the Windows registry. Please accept in order to 
   install an Explorer context menu entry "Proof read with LibreOffice" for yWriter7 files.

4. Start LibreOffice Writer. You should see a small toolbar window containing a button with
   a yWriter logo. This button is for writing the proofread file back to the yWriter project.
   Dock this toolbar anywhere for your convenience. 

5. __Optional:__  Download and install the [Courier Prime](https://quoteunquoteapps.com/courierprime).



## How to use

1. Write your novel with yWriter7. Backup entire project and close yWriter.

2  Move into your yWriter project folder, and right-click your .yw7 project file. 
   In the context menu, choose `Proof read with LibreOffice`. 

3. If everything goes well, you find an OpenDocument file named `<your yWriter project>_proof.odt`.
   Open it (double click) for proof reading. The proof reading document contains Chapter `[ChID:x]`
   and scene `[ScID:y]` markers according to yWriter 5 standard.  __Do not touch lines
   containing the markers__  if you want to be able to reimport the document into yWriter. 

4. In order to write back the proofread scenes to the yWriter project, klick the toolbar button
   with the yWriter logo, or select the menu item 
   `Tools > Add-ons > ProofYw7 > Write proofed scenes back to yWriter`.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot2.png)

If everything went well, a window will open with a success message.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw7/master/docs/Screenshots/screenshot3.png)



## How to uninstall

Move into the `ProofYw7_<version number>` folder and run `Uninstall.bat` (double click). 
You may be asked for approval to modify the Windows registry. Please accept in order to 
remove the Explorer context menu entry. 


