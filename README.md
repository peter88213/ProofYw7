# ProofYw7 - Proofread yWriter 7 scenes with LibreOffice

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw/master/docs/Screenshots/screenshot1.png)

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

3. Move into the `ProofYw7_<version number>` folder and run `Install.bat` (double click). This will copy all needed files to the right places.

4. Start LibreOffice Writer. You should see a small toolbar window containing a button with a yWriter logo. This button is for writing the proofread file back to the yWriter project. Dock this toolbar anywhere for your convenience. 

5. __Optional:__  Download and install the [Courier Prime](https://quoteunquoteapps.com/courierprime).

## How to use

1. Write your novel in yWriter 7. Make sure, the `<your yWriter project>.yw` folder contains a file named `proof.bat`. If not, copy it from `ProofYw7_<version number>\setup>` folder.

2. Close yWriter, move into the `<your yWriter project>.yw` folder, and run `proof.bat` (double click). 

3. If everything goes well, you will see an OpenDocument file named `<your yWriter project>_proof.odt`. Open it (double click) for proof reading. The proof reading document contains Chapter `[ChID:x]` and scene `[ScID:y]` markers according to yWriter 5 standard.  __Do not touch lines containing the markers__  if you want to be able to reimport the document into yWriter. 

4. In order to write back the proofread scenes to the yWriter project, klick the toolbar button with the yWriter logo, or or select the menu item _Tools > Add-ons > ProofYw7 > Write proofed scenes back to yWriter_.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw/master/docs/Screenshots/screenshot2.png)

If everything went well, a window will open with a success message.

![Screenshot: Generated ODT in LibreOffice Writer](https://raw.githubusercontent.com/peter88213/ProofYw/master/docs/Screenshots/screenshot3.png)

## How to uninstall

Move into the `ProofYw7_<version number>` folder and run `Uninstall.bat` (double click). 

