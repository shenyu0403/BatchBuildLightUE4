
pyinstaller --noconfirm ^
    --noconsole ^
    --uac-admin ^
	--distpath %CD%/Builds ^
     %CD%/Builds/build.spec

rmdir /S /Q build

Set ZNAME="Builds\B-Blue4.zip"
Set ARCHIVE=%CD%"\Builds\BBlue4\"

echo %ARCHIVE%

E:\Tools\7-Zip\7z.exe a %ZNAME% %ARCHIVE%

rmdir /S /Q "Builds\BBlue4"
