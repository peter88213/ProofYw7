@echo off
REM Installation script for the ProofYw7 software package.
REM 
REM See: https://github.com/peter88213/ProofYw7
REM License: The MIT License (https://opensource.org/licenses/mit-license.php)
REM Copyright: (c) 2020, Peter Triesberger
REM 
REM Note: This script is to be executed manually after un-packing the setup file.
REM 
REM Preconditions:
REM * Setup folder structure must exist in the working directory.
REM * LibreOffice 5.x or 6.x is installed.
REM
REM Postconditions: 
REM * The ProofYw7 Python scripts are installed in the LibreOffice user profile.
REM * The program starter "proof.bat" is generated in the setup directory.
REM * "proof.bat" is copied to all yWriter project directories within [userprofile]\Documents.

set _release=0.5.0

pushd setup

set _LibreOffice5_w64=c:\Program Files (x86)\LibreOffice 5
set _LibreOffice5_w32=c:\Program Files\LibreOffice 5
set _LibreOffice6_w64=c:\Program Files (x86)\LibreOffice
set _LibreOffice6_w32=c:\Program Files\LibreOffice

set _LibreOffice_Userprofile=AppData\Roaming\LibreOffice\4\user

echo -----------------------------------------------------------------
echo ProofYw7 (yWriter to LibreOffice) v%_release%
echo Installing software package ...
echo -----------------------------------------------------------------

rem Detect Combination of Windows and Office 

if exist "%_LibreOffice5_w64%\program\swriter.exe" goto LibreOffice5-Win64
if exist "%_LibreOffice5_w32%\program\swriter.exe" goto LibreOffice5-Win32
if exist "%_LibreOffice6_w64%\program\swriter.exe" goto LibreOffice6-Win64
if exist "%_LibreOffice6_w32%\program\swriter.exe" goto LibreOffice6-Win32
echo ERROR: No supported version of LibreOffice found!
echo Installation aborted
goto end


:LibreOffice5-Win64
set _writer=%_LibreOffice5_w64%
set _user=%USERPROFILE%\%_LibreOffice_Userprofile%
echo LibreOffice
goto settings_done

:LibreOffice5-Win32
set _writer=%_LibreOffice5_w32%
set _user=%USERPROFILE%\%_LibreOffice_Userprofile%
echo LibreOffice
goto settings_done

:LibreOffice6-Win64
set _writer=%_LibreOffice6_w64%
set _user=%USERPROFILE%\%_LibreOffice_Userprofile%
echo LibreOffice
goto settings_done

:LibreOffice6-Win32
set _writer=%_LibreOffice6_w32%
set _user=%USERPROFILE%\%_LibreOffice_Userprofile%
echo LibreOffice
goto settings_done

:settings_done

echo Copying program components to %_user%\Scripts\python ...

if not exist "%_user%\Scripts" mkdir "%_user%\Scripts"
if not exist "%_user%\Scripts\python" mkdir "%_user%\Scripts\python"
copy /y program\*.py "%_user%\Scripts\python"

echo Installing LibreOffice extension ...

"%_writer%\program\unopkg" add -f program\ProofYw7-L-%_release%.oxt

echo Creating "proof.bat" ...

echo @echo off > proof.bat
echo if exist "%_user%\Scripts\python\ProofYw7.py" goto inst_ok >> proof.bat
echo echo ERROR: ProofYw7 Software is not installed! >> proof.bat
echo goto end >> proof.bat
echo :inst_ok >> proof.bat
echo echo ProofYw7 v%_release% >> proof.bat

echo echo Starting yWriter to LibreOffice conversion ... >> proof.bat
echo "%_writer%\program\python.exe" "%_user%\Scripts\python\ProofYw7.py" >> proof.bat
echo if errorlevel 1 goto end >> proof.bat

echo exit >> proof.bat
echo :end >> proof.bat
echo pause >> proof.bat

echo "%_writer%\program\python.exe" "findyw7.py" >> findyw7.bat
call findyw7.bat
call Copyproof.bat
popd

echo -----------------------------------------------------------------
echo #
echo # Installation of ProofYw7 software package v%_release% finished.
echo #
echo # Operation: 
echo # Go into your yWriter Project folder and run "proof.bat"
echo #
echo -----------------------------------------------------------------

:end
pause