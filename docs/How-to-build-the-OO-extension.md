1. Install the package and run OpenOffice.
2. Edit ProofYw7 macros using OpenOffice's built-in macro editor.
3. Close macro editor and test the modified macros.
4. Export ProofYw7 library as _BASIC library_ to `[your local Git folder]\ProofYw7\oxt\ProofYw7` folder.
5. Compile the extension using `[your local Git folder]\ProofYw7\oxt\ProofYw7.odt`. Make sure, the correct release number is set.  
6. Edit installation files `src\Install.bat` and `src\Uninstall.bat` (at least modify release number).
7. Edit build script `tools\cs.bat` (modify release number).
8. Execute `tools\cs.bat`. This script creates a folder `[your local Git folder]\ProofYw7\build\ProofYw7_v[release number]`and puts all needed files into it. Eclipse users can execute this step via __ant__. 
9. Install the modified package and run OpenOffice for macro tests. I recommend separate virtual machines (e.g. VirtualBox) for OpenOffice 3.x and OpenOffice 4.x. and LibreOffice 5.x installations. 
10. Zip `[your local Git folder]\ProofYw7\build\ProofYw7_v[release number]` to `ProofYw7_v[release number].zip`.