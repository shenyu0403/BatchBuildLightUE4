
pyinstaller --noconfirm ^
    --noconsole ^
    --uac-admin ^
	--distpath %CD% ^
     %CD%/build.spec

rmdir /S /Q build

Set ZNAME="B-Blue4.zip"
Set ARCHIVE=%CD%"\BBlue4\"

echo %ARCHIVE%

E:\Tools\7-Zip\7z.exe a %ZNAME% %ARCHIVE%

rmdir /S /Q "BBlue4"
